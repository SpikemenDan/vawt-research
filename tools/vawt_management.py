"""Management tooling shared by every VAWT research folder.

    python tools/vawt_management.py refresh "(Default) Research Papers"
    python tools/vawt_management.py init    "(Helical) Research Papers"

The workbook <type>/!management/metadata.xlsx is the only metadata store. Edit the data
columns of its Metadata sheet directly (Status, colours and the other sheets are
generated, so changes to them are overwritten), then run `refresh`:

refresh  Re-reads the Metadata sheet and sources.csv, checks every row against the data
         CSVs on disk, and rewrites the workbook: green = done, yellow = needs a check,
         no fill = pending, one blank row between sources, plus Summary, To check,
         Sources and Legend sheets. Close the workbook in Excel first.
init     Creates the empty folder skeleton for a new rotor type.

Needs openpyxl (pip install openpyxl).
"""
import csv
import datetime
import glob
import os
import sys

META_COLS = ["Curve_ID", "filename", "N", "cToR", "U_m_s", "Re_D", "Re_rot", "alpha_p", "Pitch_direction",
             "Surface_Finish", "Pressure_bar", "Foil_Profile", "Struts", "Strut_loss", "Medium", "Re_basis",
             "Pitch_basis", "assumed_mu_Pa_s", "assumed_rho_kg_m3", "Action", "Notes"]
SOURCE_COLS = ["Source_ID", "Rotor", "Reference", "Verification", "Priority", "Experimental_content",
               "Extraction_target", "Known_properties", "Audit_notes", "Source_URL"]

ACTIONS = [
    ("Use", "Done", "Data CSV exists and the metadata was checked against the paper."),
    ("Use - check", "Check", "Data CSV exists, but a known issue needs review before use. The Notes column says what to do."),
    ("Extract", "Pending", "Series is wanted; the data CSV has not been created yet."),
    ("Capture figure", "Pending", "Figure screenshot is still needed before extraction."),
    ("Review repeat", "Pending", "May duplicate another curve; compare before extracting. Delete the row if it is a duplicate."),
]
RE_BASIS = [
    ("reported", "Source states Re_D; stored in Re_D."),
    ("reported approximate", "Source gives a rounded or approximate Re_D."),
    ("estimated", "Constant Re_D = rho*U*D/mu from U, D and the assumed air properties."),
    ("pointwise from U", "Re_D varies by row = D*U/nu; Re_D blank here, filled on each data row."),
    ("pointwise from Re_rot", "Re_D = 2*Re_rot/(cToR*TSR) on each data row; Re_D blank here."),
    ("estimated from peak TSR and reported Re_rot", "Re_D = 2*Re_rot/(cToR*TSR_peak), stored as one constant."),
]
COLUMN_HELP = {
    "Curve_ID": "SourceYear-Cxxx. Unique key; C-numbers restart at C001 per source and stay consecutive.",
    "filename": "Data CSV name: SourceYear (Fig 4) (N = 3) (cToR = 0.085714) (C001).csv  (Tab for tables).",
    "N": "Number of blades.",
    "cToR": "Chord / radius. Blank = unknown, never zero.",
    "U_m_s": "Free-stream speed. Blank if it varies by row (then it is a data column).",
    "Re_D": "Diameter Reynolds number. Blank if it varies by row.",
    "Re_rot": "Rotational chord Reynolds number, omega*R*c/nu, as reported.",
    "alpha_p": "Fixed blade pitch, degrees. Blank = not assigned, never zero.",
    "Pitch_direction": "toe-in / toe-out where the source gives one.",
    "Surface_Finish": "rough / smooth where the source gives one.",
    "Pressure_bar": "Working-fluid static pressure for pressurised tests.",
    "Foil_Profile": "NACA0015 style (no space); add qualifiers after the code.",
    "Struts": "yes / no: physical blade-support struts or spokes.",
    "Strut_loss": "corrected if strut drag was removed from the measured torque.",
    "Medium": "Working fluid.",
    "Re_basis": "How Re_D was obtained (vocabulary below).",
    "Pitch_basis": "Where alpha_p and its sign convention come from.",
    "assumed_mu_Pa_s": "Assumed dynamic viscosity. Filled only where an assumption was actually used.",
    "assumed_rho_kg_m3": "Assumed density. Filled only where an assumption was actually used.",
    "Action": "Workflow state (vocabulary below). Documentation only, not a model input.",
    "Notes": "Source pages, geometry, formulas and caveats. A 'Check:' sentence says what to do for yellow rows.",
}
NUMERIC = {"N": "0", "cToR": "0.000000", "U_m_s": "0.00##", "Re_D": "#,##0", "Re_rot": "#,##0", "alpha_p": "0.##",
           "Pressure_bar": "0.##", "assumed_mu_Pa_s": "0.00E+00", "assumed_rho_kg_m3": "0.00"}

LOG_SKELETON = """# {title}: management log

## 1. Files in this folder

| File | Purpose |
|---|---|
| `metadata.xlsx` | One row per retained experimental curve. Only metadata store; green = done, yellow = needs a check. Edit the Metadata sheet, then run `python tools/vawt_management.py refresh "{folder}"`. |
| `sources.csv` | One row per paper or lead, including ones not yet extracted. |
| `ASSUMPTIONS_AND_CHANGES.md` | This log. |

## 2. Conventions

See `MANAGEMENT_TEMPLATE.md` at the repository root.

## 3. Decisions and assumptions

1. (none yet)

## 4. Source status

| Source | Curves | CSVs | Status |
|---|---|---|---|

## 5. Open items

- (none yet)

## 6. Change history

- {today}: folder created from the template.
"""


def _cell(v):
    if v is None:
        return ""
    if isinstance(v, float) and v == int(v) and abs(v) >= 1:
        return int(v)
    if isinstance(v, str):
        return v.strip()
    return v


def load_metadata(mdir):
    """Return rows as dicts. Reads metadata.xlsx; falls back to metadata.csv for a first migration."""
    xp, cp = os.path.join(mdir, "metadata.xlsx"), os.path.join(mdir, "metadata.csv")
    if os.path.exists(xp):
        from openpyxl import load_workbook
        ws = load_workbook(xp, data_only=True)["Metadata"]
        hdr = [c.value for c in ws[1]]
        if hdr != ["Status"] + META_COLS:
            sys.exit("Metadata sheet columns differ from the template: %s" % hdr)
        out = []
        for row in ws.iter_rows(min_row=2, values_only=True):
            d = dict(zip(META_COLS, [_cell(v) for v in row[1:]]))
            if d["Curve_ID"] != "":
                out.append(d)
        return out
    if os.path.exists(cp):
        with open(cp, encoding="utf-8-sig", newline="") as f:
            rows = list(csv.reader(f))
        if rows[0] != META_COLS:
            sys.exit("metadata.csv columns differ from the template")
        out = []
        for r in rows[1:]:
            if any(c.strip() for c in r):
                d = dict(zip(META_COLS, r))
                for c in NUMERIC:
                    try:
                        fv = float(d[c]) if d[c] != "" else None
                    except ValueError:
                        fv = None
                    if fv is not None:
                        d[c] = int(fv) if c in ("N", "Re_D", "Re_rot") and fv == int(fv) else fv
                out.append(d)
        return out
    return []


def load_sources(mdir):
    p = os.path.join(mdir, "sources.csv")
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    if rows[0] != SOURCE_COLS:
        sys.exit("sources.csv columns differ from the template: %s" % rows[0])
    return [dict(zip(SOURCE_COLS, r)) for r in rows[1:] if any(c.strip() for c in r)]


def status_of(action, exists):
    for a, s, _ in ACTIONS:
        if a == action:
            if s in ("Done", "Check") and not exists:
                return "Pending", "Action says data exists but no CSV found"
            if s == "Pending" and exists:
                return "Done", "CSV exists but Action says it is not extracted"
            return s, None
    return "Pending", "Unknown Action: " + str(action)


def check_text(notes):
    """The 'Check:' sentence of a Notes cell (up to the next ' | '), or ''."""
    i = str(notes).find("Check:")
    if i < 0:
        return ""
    j = str(notes).find(" | ", i)
    return str(notes)[i:j if j > 0 else None].strip()


def write_workbook(folder, recs, srcs):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter

    mdir = os.path.join(folder, "!management")
    files = {os.path.basename(p) for p in glob.glob(os.path.join(folder, "**", "*.csv"), recursive=True)
             if "!management" not in p}
    warnings = []
    for r in recs:
        r["_status"], w = status_of(r["Action"], r["filename"] in files)
        if w:
            warnings.append("%s: %s" % (r["Curve_ID"], w))
        r["_src"] = r["Curve_ID"].split("-")[0]
        if r["_status"] == "Check" and not check_text(r["Notes"]):
            warnings.append("%s: yellow row has no 'Check:' note saying what to do" % r["Curve_ID"])
    ids = [r["Curve_ID"] for r in recs]
    for i in sorted({x for x in ids if ids.count(x) > 1}):
        warnings.append("duplicate Curve_ID " + i)
    for fn in sorted(files - {r["filename"] for r in recs}):
        warnings.append("data file not in metadata: " + fn)
    order = []
    for r in recs:
        if r["_src"] not in order:
            order.append(r["_src"])
    for s in order:
        nums = sorted(int(r["Curve_ID"].split("-C")[1]) for r in recs if r["_src"] == s)
        if nums != list(range(1, len(nums) + 1)):
            warnings.append("%s: Curve_ID numbers are not consecutive from C001" % s)

    GREEN, YELLOW = "C6EFCE", "FFFF99"
    fills = {"Done": PatternFill("solid", fgColor=GREEN), "Check": PatternFill("solid", fgColor=YELLOW)}
    font_c = {"Done": "006100", "Check": "7F6000", "Pending": "595959"}
    head_fill = PatternFill("solid", fgColor="1F3864")
    head_font = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
    base = Font(name="Calibri", size=10)
    thin = Side(style="thin", color="D9D9D9")
    med = Side(style="medium", color="7F7F7F")
    h1 = Font(name="Calibri", size=12, bold=True, color="1F3864")

    def header(ws, row, labels):
        for i, lab in enumerate(labels, 1):
            c = ws.cell(row=row, column=i, value=lab)
            c.fill, c.font = head_fill, head_font
            c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.row_dimensions[row].height = 30

    wb = Workbook()
    # ---------------- Summary
    ws = wb.active
    ws.title = "Summary"
    title = os.path.basename(folder.rstrip("\\/")).replace(" Research Papers", "").strip("()")
    ws["A1"] = "%s VAWT research data" % title
    ws["A1"].font = Font(name="Calibri", size=16, bold=True, color="1F3864")
    ws["A2"] = "Generated %s by tools/vawt_management.py refresh. Edit the Metadata sheet, then refresh." % datetime.date.today()
    ws["A2"].font = Font(name="Calibri", size=9, italic=True, color="595959")
    tot = {s: sum(1 for r in recs if r["_status"] == s) for s in ("Done", "Check", "Pending")}
    for i, (lab, key) in enumerate([("Done", "Done"), ("Needs check", "Check"), ("Pending", "Pending")]):
        c = ws.cell(row=4, column=1 + i * 2, value=lab)
        c.font = Font(name="Calibri", size=10, bold=True, color=font_c[key])
        n = ws.cell(row=5, column=1 + i * 2, value=tot[key])
        n.font = Font(name="Calibri", size=22, bold=True, color=font_c[key])
        if key in fills:
            c.fill = n.fill = fills[key]
    ws.cell(row=4, column=7, value="Total curves").font = Font(name="Calibri", size=10, bold=True)
    ws.cell(row=5, column=7, value=len(recs)).font = Font(name="Calibri", size=22, bold=True)
    header(ws, 7, ["Source", "Curves", "Done", "Needs check", "Pending", "% done"])
    srow = 8
    counts = {}
    for s in order:
        rs = [r for r in recs if r["_src"] == s]
        d, ch, p = (sum(1 for r in rs if r["_status"] == k) for k in ("Done", "Check", "Pending"))
        counts[s] = (len(rs), d, ch, p)
        key = "Done" if d == len(rs) else ("Check" if ch and not p else "Pending")
        for i, v in enumerate([s, len(rs), d, ch, p, d / len(rs)], 1):
            c = ws.cell(row=srow, column=i, value=v)
            c.font = base
            c.border = Border(bottom=thin)
            if key in fills and i == 1:
                c.fill = fills[key]
        ws.cell(row=srow, column=6).number_format = "0%"
        srow += 1
    for i, v in enumerate(["Total", len(recs), tot["Done"], tot["Check"], tot["Pending"], tot["Done"] / max(len(recs), 1)], 1):
        c = ws.cell(row=srow, column=i, value=v)
        c.font = Font(name="Calibri", size=10, bold=True)
        c.border = Border(top=med)
    ws.cell(row=srow, column=6).number_format = "0%"
    if warnings:
        ws.cell(row=srow + 2, column=1, value="Consistency warnings").font = Font(name="Calibri", size=10, bold=True, color="9C0006")
        for i, w in enumerate(warnings, 1):
            ws.cell(row=srow + 2 + i, column=1, value=w).font = Font(name="Calibri", size=9, color="9C0006")
    for col, w in zip("ABCDEFG", (30, 10, 10, 13, 10, 10, 14)):
        ws.column_dimensions[col].width = w
    ws.sheet_view.showGridLines = False

    # ---------------- Metadata (one blank row between sources)
    wm = wb.create_sheet("Metadata")
    header(wm, 1, ["Status"] + META_COLS)
    row_i = 1
    prev = None
    for r in recs:
        row_i += 1
        if prev is not None and r["_src"] != prev:
            row_i += 1
        prev = r["_src"]
        st = r["_status"]
        for j, v in enumerate([st] + [r[c] for c in META_COLS], 1):
            c = wm.cell(row=row_i, column=j, value=v if v != "" else None)
            col = META_COLS[j - 2] if j > 1 else "Status"
            c.font = base
            c.border = Border(bottom=thin)
            if st in fills:
                c.fill = fills[st]
            if j == 1:
                c.font = Font(name="Calibri", size=10, bold=True, color=font_c[st])
                c.alignment = Alignment(horizontal="center")
            elif col in NUMERIC and v != "":
                c.number_format = NUMERIC[col]
                c.alignment = Alignment(horizontal="center")
            elif col in ("Pitch_direction", "Surface_Finish", "Struts", "Strut_loss", "Medium"):
                c.alignment = Alignment(horizontal="center")
    widths = {"Status": 10, "Curve_ID": 24, "filename": 64, "N": 5, "cToR": 10, "U_m_s": 8, "Re_D": 12, "Re_rot": 10,
              "alpha_p": 8, "Pitch_direction": 11, "Surface_Finish": 10, "Pressure_bar": 9, "Foil_Profile": 30,
              "Struts": 8, "Strut_loss": 11, "Medium": 8, "Re_basis": 24, "Pitch_basis": 34,
              "assumed_mu_Pa_s": 11, "assumed_rho_kg_m3": 11, "Action": 15, "Notes": 90}
    for j, name in enumerate(["Status"] + META_COLS, 1):
        wm.column_dimensions[get_column_letter(j)].width = widths[name]
    wm.freeze_panes = "C2"
    wm.auto_filter.ref = "A1:%s%d" % (get_column_letter(len(META_COLS) + 1), max(row_i, 2))

    # ---------------- To check
    wc = wb.create_sheet("To check")
    header(wc, 1, ["Curve_ID", "Source", "What to do (then set Action to Use and refresh)"])
    k = 1
    for r in recs:
        if r["_status"] != "Check":
            continue
        k += 1
        for j, v in enumerate([r["Curve_ID"], r["_src"], check_text(r["Notes"])], 1):
            c = wc.cell(row=k, column=j, value=v)
            c.font = base
            c.fill = fills["Check"]
            c.alignment = Alignment(vertical="top", wrap_text=True)
            c.border = Border(bottom=thin)
        wc.row_dimensions[k].height = min(15 * max(1, -(-len(check_text(r["Notes"])) // 120)), 200)
    if k == 1:
        wc.cell(row=2, column=1, value="Nothing needs checking.").font = base
    wc.column_dimensions["A"].width = 24
    wc.column_dimensions["B"].width = 18
    wc.column_dimensions["C"].width = 130
    wc.freeze_panes = "A2"

    # ---------------- Sources
    wsr = wb.create_sheet("Sources")
    header(wsr, 1, ["Source_ID", "Curves", "Done", "Check", "Pending"] + SOURCE_COLS[1:])
    wrap_cols = {"Reference": 34, "Verification": 28, "Experimental_content": 44, "Extraction_target": 30,
                 "Known_properties": 44, "Audit_notes": 70, "Rotor": 22, "Priority": 12, "Source_URL": 34}
    for i, s in enumerate(srcs, 2):
        n, d, ch, p = counts.get(s["Source_ID"], (0, 0, 0, 0))
        key = "Done" if n and d == n else ("Check" if ch and not p else None)
        vals = [s["Source_ID"], n, d, ch, p] + [s[c] for c in SOURCE_COLS[1:]]
        lines = 1
        for j, v in enumerate(vals, 1):
            c = wsr.cell(row=i, column=j, value=v)
            c.font = base
            c.alignment = Alignment(vertical="top", wrap_text=True, horizontal="center" if 2 <= j <= 5 else "left")
            c.border = Border(bottom=thin)
            if key and j == 1:
                c.fill = fills[key]
            if j >= 6:
                lines = max(lines, -(-len(str(v)) // int(wrap_cols[SOURCE_COLS[j - 5]] * 1.1)))
        wsr.row_dimensions[i].height = min(15 * lines, 400)
    wsr.column_dimensions["A"].width = 24
    for col in "BCDE":
        wsr.column_dimensions[col].width = 8
    for j, name in enumerate(SOURCE_COLS[1:], 6):
        wsr.column_dimensions[get_column_letter(j)].width = wrap_cols[name]
    wsr.freeze_panes = "B2"

    # ---------------- Legend
    wl = wb.create_sheet("Legend")
    r0 = 1
    wl.cell(row=r0, column=1, value="Row colours").font = h1
    for k, (lab, key, txt) in enumerate([("Done", "Done", "Data CSV exists and metadata verified."),
                                         ("Yellow", "Check", "Data CSV exists; a known issue needs review (see the To check sheet)."),
                                         ("Pending", "Pending", "No data CSV yet.")], 1):
        a = wl.cell(row=r0 + k, column=1, value=lab)
        a.font = Font(name="Calibri", size=10, bold=True, color=font_c[key])
        if key in fills:
            a.fill = fills[key]
        wl.cell(row=r0 + k, column=3, value=txt).font = base
    r0 += 6
    wl.cell(row=r0, column=1, value="Action vocabulary").font = h1
    header(wl, r0 + 1, ["Action", "Status", "Meaning"])
    for k, (a, s, t) in enumerate(ACTIONS, 2):
        for j, v in enumerate((a, s, t), 1):
            wl.cell(row=r0 + k, column=j, value=v).font = base
    r0 += len(ACTIONS) + 4
    wl.cell(row=r0, column=1, value="Re_basis vocabulary").font = h1
    header(wl, r0 + 1, ["Re_basis", "", "Meaning"])
    for k, (a, t) in enumerate(RE_BASIS, 2):
        wl.cell(row=r0 + k, column=1, value=a).font = base
        wl.cell(row=r0 + k, column=3, value=t).font = base
    r0 += len(RE_BASIS) + 4
    wl.cell(row=r0, column=1, value="Metadata columns").font = h1
    header(wl, r0 + 1, ["Column", "", "Meaning"])
    for k, col in enumerate(META_COLS, 2):
        wl.cell(row=r0 + k, column=1, value=col).font = Font(name="Calibri", size=10, bold=True)
        wl.cell(row=r0 + k, column=3, value=COLUMN_HELP[col]).font = base
    wl.column_dimensions["A"].width = 30
    wl.column_dimensions["B"].width = 10
    wl.column_dimensions["C"].width = 110
    wl.sheet_view.showGridLines = False

    out = os.path.join(mdir, "metadata.xlsx")
    try:
        wb.save(out)
    except PermissionError:
        sys.exit("Cannot write %s. Close it in Excel and run again." % out)
    print("wrote", out)
    print("curves %d: done %d, check %d, pending %d" % (len(recs), tot["Done"], tot["Check"], tot["Pending"]))
    for w in warnings:
        print("WARNING:", w)
    return 1 if warnings else 0


def refresh(folder):
    mdir = os.path.join(folder, "!management")
    recs = load_metadata(mdir)
    if not recs:
        print("note: no metadata rows found")
    return write_workbook(folder, recs, load_sources(mdir))


def init(folder):
    if os.path.exists(folder):
        sys.exit("already exists: " + folder)
    mdir = os.path.join(folder, "!management")
    os.makedirs(mdir)
    os.makedirs(os.path.join(folder, "!archive"))
    with open(os.path.join(mdir, "sources.csv"), "w", newline="", encoding="utf-8") as f:
        csv.writer(f, lineterminator="\r\n").writerow(SOURCE_COLS)
    name = os.path.basename(folder.rstrip("\\/")).replace(" Research Papers", "").strip("()")
    with open(os.path.join(mdir, "ASSUMPTIONS_AND_CHANGES.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(LOG_SKELETON.format(title=name, folder=os.path.basename(folder), today=datetime.date.today()))
    write_workbook(folder, [], [])
    print("created", folder)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if len(sys.argv) != 3 or cmd not in ("refresh", "init"):
        sys.exit(__doc__)
    sys.exit(refresh(sys.argv[2]) if cmd == "refresh" else init(sys.argv[2]))
