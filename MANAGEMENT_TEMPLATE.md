# Template for a VAWT research folder

Every rotor type (default/H-type, troposkein, and any new one) uses the same layout, file names, columns and vocabulary, so a new type is a copy of this pattern.

## Start a new type

```bash
python tools/vawt_management.py init "(Helical) Research Papers"
```

This creates the folder below with an empty, correctly-headed `metadata.xlsx` and `sources.csv`. Name the folder `(<Type>) Research Papers`; the type is identified only by this folder name.

## Layout

```
(<Type>) Research Papers/
  !management/
    metadata.xlsx                one row per retained curve; the only metadata store (no metadata CSV)
    sources.csv                  one row per paper or lead
    ASSUMPTIONS_AND_CHANGES.md   decisions, source status, open items, change history
  !archive/
    SourceYear/
      SourceYear.pdf
      data/
        SourceYear (Fig 4).png                                       figure screenshot
        SourceYear (Fig 4) (N = 3) (cToR = 0.085714) (C001).csv     one curve per CSV
```

Keep optional extras (for example a literature review PDF) in `!management/`. Edit the `Metadata` sheet of `metadata.xlsx` directly, then recompute status and colours:

```bash
python tools/vawt_management.py refresh "(<Type>) Research Papers"
```

Close the workbook in Excel first. `refresh` checks `Action` against the data files on disk and prints a warning for any disagreement, a duplicate or non-consecutive Curve_ID, or a yellow row with no `Check:` note. It regenerates the `Status` column, the colours, one blank row between sources, and the Summary, To check, Sources and Legend sheets, so do not edit those by hand.

## Workflow for each new paper

1. Add the paper to `sources.csv`. Identify the experimental Cp-TSR curves and repeated baselines before asking for any digitization.
2. Audit geometry and conditions against the PDF (blade count, radius, chord, airfoil, speeds, Re, pitch, struts). Settle open assumptions one at a time and record them in the log.
3. Add one `Metadata` row per distinct curve. Skip a figure that only repeats a curve you already have; do not list duplicates. IDs are `SourceYear-C001`, numbered in figure and condition order. Leave anything unknown blank.
4. Save the figure screenshot, then create each data CSV. Put TSR and Cp first, then the constants from metadata; anything that varies by row (Re_D, U) goes on every row.
5. Set `Action` to `Use` once the CSV exists and was checked, or `Use - check` if an issue remains. Rebuild the workbook.
6. Log decisions, assumptions, source conflicts and edits in `ASSUMPTIONS_AND_CHANGES.md`. Original PDFs and raw measurements stay intact.

## Metadata sheet columns (fixed order)

`Curve_ID, filename, N, cToR, U_m_s, Re_D, Re_rot, alpha_p, Pitch_direction, Surface_Finish, Pressure_bar, Foil_Profile, Struts, Strut_loss, Medium, Re_basis, Pitch_basis, assumed_mu_Pa_s, assumed_rho_kg_m3, Action, Notes`

Rules: one blank row between sources (added by `refresh`). Blank means unknown, never zero. Curve_ID numbers stay consecutive from C001 within a source; renumber after deleting a row. `Action` and `Notes` are documentation, not numerical inputs. The full column dictionary is on the Legend sheet of every workbook.

## Vocabulary

**Action**

| Value | Meaning | Workbook colour |
|---|---|---|
| `Use` | CSV exists and the metadata was checked against the paper | green |
| `Use - check` | CSV exists but a known issue needs review; the `Check:` sentence in Notes says what to do and is copied to the To check sheet | yellow |
| `Extract` | wanted, CSV not created yet | none |
| `Capture figure` | screenshot still needed | none |
| `Review repeat` | may duplicate another curve; compare first | none |

**Re_basis**

| Value | Meaning |
|---|---|
| `reported` / `reported approximate` | source states Re_D; stored in `Re_D` |
| `estimated` | constant Re_D = rho U D / mu from U, D and assumed air; mu and rho columns filled |
| `pointwise from U` | Re_D = D U / nu on each data row; `Re_D` blank |
| `pointwise from Re_rot` | Re_D = 2 Re_rot / (cToR TSR) on each data row; `Re_D` blank |
| `estimated from peak TSR and reported Re_rot` | one constant from the peak TSR |

## Shared conventions

- Filenames: `SourceYear (Fig 4) (N = 3) (cToR = 0.085714) (C001).csv`; panels keep their letter (`Fig 11a`); numerical tables use `Tab`. Unknown c/R reads `cToR = unknown` and stays blank until resolved.
- Assumed air where needed: mu = 1.80E-05 Pa s, rho = 1.20 kg/m3, nu = 1.50E-05 m2/s. Fill the two assumption columns only on rows that use them.
- Foil names are written `NACA0015` (no space) with qualifiers after the code.
- Pitch magnitude and toe-in/toe-out direction are stored separately; no cross-paper sign convention is imposed.
- Do not borrow geometry from a different paper, even by the same group.
