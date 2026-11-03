# Troposkein VAWT: management log

Curved-blade (Darrieus) rotors. Last updated 2026-11-02.

## 1. Files in this folder

| File | Purpose |
|---|---|
| `metadata_troposkein.xlsx` | One row per retained experimental curve (41). The only metadata store; there is no metadata CSV. Green = done, yellow = needs a check (the "To check" sheet says what to do), no fill = pending. One blank row separates sources. After editing the Metadata sheet, run `python tools/vawt_management.py refresh "(Troposkein) Research Papers"` to recompute status and colours. |
| `sources.csv` | One row per paper or lead, including candidates not yet extracted. |
| `Troposkein_Dataset_Review.pdf` | Literature review PDF supplied with the dataset (kept as reference). |
| `ASSUMPTIONS_AND_CHANGES.md` | This log. |

The old `rename_map_troposkein.csv` was retired on 2026-11-02; filenames are final and `metadata_troposkein.xlsx` lists them. The earlier Excel workbook with a "Re_D Calculations" tab is not in the repository; its content is section 5 below and the Re_D instruction in each row's Notes.

## 2. Conventions

- **Filename:** `SourceYear (Fig 4) (N = 3) (cToR = 0.085714) (C001).csv`. Numerical tables use `Tab` instead of `Fig`. Known c/R is rounded to six decimals; source dimensions are in Notes.
- **Curve_ID:** `SourceYear-C001`. C-numbers restart at C001 for each source, follow source / figure / condition order, and carry no physics. Keep assigned IDs when adding curves.
- **Match metadata to a data file** by filename or Curve_ID. Copy the constants you need into the data CSV; TSR and Cp are the varying columns. Store anything that varies by row (Re_D, U) on each row, never one point copied down.
- **Blank means unknown or not assigned, never zero.** An unknown c/R would appear as `cToR = unknown` in a filename and stay blank in the metadata; none is unknown now.
- **Action** (documentation only): `Use` = CSV exists and metadata checked against the paper; `Use - check` = CSV exists but a known issue needs review; `Extract`, `Capture figure`, `Review repeat` = not extracted yet.
- **Re_basis:** `pointwise from Re_rot`, `pointwise from U`, `estimated`. Definitions are on the Legend sheet of the workbook; the exact formula is in each row's Notes.
- **Assumed air:** nu = 1.50E-05 m2/s (mu 1.80E-05 Pa s, rho 1.20 kg/m3). `assumed_mu_Pa_s` and `assumed_rho_kg_m3` are filled only on rows where this assumption feeds Re_D (Blackwell fixed-U, Muraca, Battisti2018). Do not overwrite the measured density used to calculate Cp.

## 3. Decisions and assumptions

1. **Nominal air viscosity** was approved for direct speed calculations (see conventions). Field-site data with unresolved geometry are not given fabricated constants.
2. **Re_rot** is the reported rotational chord Reynolds number, omega R c / nu. It is not a diameter Reynolds number. Where it applies, Re_D = 2 Re_rot / [(c/R) TSR], evaluated point by point; no viscosity is needed. Re_D stays blank in the metadata.
3. **Fixed-speed Blackwell runs** use Re_D = rho U (2R) / mu, a constant per curve. The Muraca NASA Fig 8 pools speeds, so it has no curve-wide Re_D.
4. **Pitch:** blank is not zero. Rotor tilt, virtual incidence and manufacturing twist are not substituted for a uniform physical alpha_p. No cross-paper sign convention is imposed.
5. **Solidity** is recorded in Notes with its source definition. Blade-area solidity is not the notebook's N(c/R)/(2 pi). Mixed-chord and curved blades need explicit geometry conventions.
6. **Negative Cp** is preserved. A non-negative subset, if wanted, is made in a working copy with affected points documented.
7. **Cp validation:** do not automatically discard Cp > 0.593; check area normalisation, confinement and corrections first.
8. **Sheldahl1980 C004/C005 (2026-11-02):** the two data files were swapped relative to the metadata. Fig 9 gives circles = 162.5 rpm (Re_c 3.3e5) and squares = 175 rpm (3.56e5). The file holding the squares (TSR 2.02-9.92) was named C004. The two files were exchanged so C004 = 162.5 rpm (Re_rot 330000) and C005 = 175 rpm (356000), matching the metadata. No cell values changed.
9. **Sheldahl1977 (2026-11-02):** c/R is the nominal equatorial ratio 0.19 m / 2.5 m = 0.076, not a verified uniform chord. Data files were renamed from `cToR = unknown` to `cToR = 0.076` and reformatted with a header, N, cToR, Re_rot and pointwise Re_D = 2 Re_rot / (cToR TSR), the same layout as Blackwell. The earlier rpm-based estimate (nominal D = 5 m, nu = 1.50E-05) was dropped so every source uses one method; it differed by about 20% because Re_rot reflects the 1658 m test site's thinner air.
10. **Battisti2016 geometry** (c = 0.101 m, R_eq = 1.014 m, c/R = 0.099606, DU-06-W200) comes from the companion Energy paper. Battisti2018 dimensions must not be borrowed.
11. **Importer and notebook:** this folder is independent of the default folder's tables. Notebook ingestion was not edited or tested.
12. **Sheldahl1977 re-digitized and Blackwell Fig 19 confirmed (2026-11-02):** the user re-digitized all four Sheldahl1977 Fig 9 series and confirmed the Blackwell Fig 19 speeds (7 and 9 m/s). Checked against the Fig 9 legend by endpoint and peak: 125 rpm squares end at TSR 6.69 (Cp -0.061); 150b triangles end at 6.73, peak 0.237; 150a circles end at 7.32, peak 0.272; 162.5 rpm diamonds end at 7.27, peak 0.238. The new C002 file held the circles and C003 the triangles, so the two files were exchanged to match the metadata (C002 = 150b, Re_rot 380000; C003 = 150a, 400000), as for Sheldahl1980. The files were reformatted with a header, N, cToR, Re_rot and pointwise Re_D. The nominal c/R 0.076 stays accepted, as in the original `Use with nominal equatorial geometry` action. All of these rows are now `Use` (green).
13. **Battisti2016 extracted (2026-11-02):** Tables 1-4 were read from the user's screenshots and every TSR_eq, CQ,aero, CTX and CTY value (58 rows, signs included) was cross-checked against the PDF text layer, where the minus sign is a private glyph. The tables give CQ,aero, not Cp, so Cp = TSR_eq x CQ,aero is calculated and Re_D = 2 Re_rot / (cToR TSR) per row, with cToR 0.099606 and Re_rot 138000 / 205000. Peak Cp: Tab 1 0.275 at TSR 3.53; Tab 2 0.345 at 3.38; Tab 3 0.234 at 3.29; Tab 4 0.315 at 3.54. High-TSR points have negative Cp (for example Tab 2, TSR 8.17, Cp -1.19), which is kept as printed. One workbook and one CSV per table are in `Battisti2016/data/`.

## 4. Source status

| Source | Rotor | Curves | CSVs | Status |
|---|---|---|---|---|
| Battisti2016 | DeepWind demonstrator | 4 | 4 | Done (Cp calculated from CQ,aero) |
| Battisti2018 | Troposkien vs H-rotor | 1 | 1 | Done |
| Blackwell1976 | Sandia 2-m | 26 | 26 | Done |
| Muraca1976 | NASA 14-ft | 1 | 1 | Done |
| Sheldahl1977 | Sandia 5-m, original blades | 4 | 4 | Done (nominal c/R 0.076) |
| Sheldahl1980 | Sandia 5-m, extruded NACA0015 | 5 | 5 | Done |
| **Total** | | **41** | **41** | 41 done, 0 to check, 0 pending |

Other sources in `sources.csv` (Ashwill1992, Read1986, SouthRangi, WorstellAddendum) have no curves yet. The Sandia 17-m and 34-m reports were not among the audited papers, so their figure completeness is not certified.

Supporting references are not tracked in `sources.csv`; they are named here and in the notes instead: **Battisti2016Energy** (Energy 111 (2016) 484-497, DOI 10.1016/j.energy.2016.05.080; the companion paper of the same DeepWind campaign, which supplies the Battisti2016 geometry and is never counted as a separate experiment) and **VeersCompilation** (Sandia selected-papers compilation, SAND90-1615; a bibliographic lead only).

### Battisti2016

Tables 1-4, PDF pp4-5; 4 curves (200/300 rpm, upright and 15-degree tilt). Figs 3-4 repeat the torque-coefficient data; Figs 5-6 are thrust, not performance. Cp = TSReq x CQ,aero; the tables list CQ,aero, so convert before use. Tables are preferred over figure digitization.

### Battisti2018

Table 9, PDF p19: one troposkien curve (Fig 10). Exclude H-shaped data and wake/load figures. Use per-row rpm, U, rho and Qaero: omega = 2 pi rpm / 60; TSR = omega x 0.755 / U; Cp = Qaero x omega / (0.5 rho x 1.5 x U^3). N = 3, c = 0.085 m, R_eq = 0.755 m, c/R = 0.112583 (Tables 3 and 5, pp4-5). No blade-support spokes (hubs and shaft remain). No blockage correction; bearing losses corrected. The 174350 Reynolds value is the nominal zero-wind Table 6 reference.

### Blackwell1976

Figs 6-10 (PDF pp34-38): 16 fixed-rotational-Re curves. Figs 15-19 (pp43-47): 10 fixed-U curves. Table I (p25): measured R = 0.9798 m, A = 2.5944 m2, chords 0.08815 / 0.07346 / 0.05877 m, giving c/R 0.089967 / 0.074974 / 0.059982. Use the measured radius, not a nominal 1 m. Fig 10's legend resolves a conflicting Table I entry. Filled peak-torque markers belong to their parent curve. Figs 11-14 and 20 reorganize runs and Fig 21 adds reference data; do not import them again.

| Curve | Figure | Series |
|---|---|---|
| C001-C003 | Fig 6 (N=3, c/R 0.089967) | 180 / 267 / 500 rpm; Re_c 104000 / 150000 / 290000 |
| C004-C006 | Fig 7 (N=3, c/R 0.074974) | 216 / 320 / 600 rpm; Re_c 101000 / 151000 / 278000 |
| C007-C009 | Fig 8 (N=3, c/R 0.059982) | 270 / 400 / 525 rpm; Re_c 101000 / 154000 / 200000 |
| C010-C013 | Fig 9 (N=2, c/R 0.089967) | 180 / 267 / 350 / 500 rpm; Re_c 106000 / 156000 / 204000 / 290000 |
| C014-C016 | Fig 10 (N=2, c/R 0.059982) | 267 / 400 / 525 rpm; Re_c 104000 / 155000 / 200000 |
| C017-C018 | Fig 15 (N=3, c/R 0.089967) | U 9 / 11 m/s |
| C019-C020 | Fig 16 (N=3, c/R 0.074974) | U 9 / 11 m/s |
| C021-C022 | Fig 17 (N=3, c/R 0.059982) | U 7 / 9 m/s |
| C023-C024 | Fig 18 (N=2, c/R 0.089967) | U 9 / 11 m/s |
| C025-C026 | Fig 19 (N=2, c/R 0.059982) | U 7 / 9 m/s |

### Muraca1976

Fig 8 (PDF p27): NASA open circles only, one mixed-speed dataset; exclude filled NAE/NRC circles and analytical lines. Table I (p18) pairs wind speed, Cp and TSR for each run and is used instead of digitizing Fig 8. N = 2, D = 4.2672 m, R = 2.1336 m. Average chord 5.58 in = 0.141732 m (the printed 0.0142 m is a conversion error); c/R = 0.066429. Blades are nominal NACA0012, about 15% thick, and one blade is twisted (about 2 deg average incidence); twist is not uniform pitch. Run 105 has no Cp or TSR; do not invent values.

### Sheldahl1977

Fig 9 (PDF p25): four campaigns, 125 / 150b / 150a / 162.5 rpm (Re_rot 340000 / 380000 / 400000 / 410000), sigma = 0.26. Original blades: curved NACA0012 section c = 0.19 m with streamlined steel end sections c = 0.10 m (PDF p13). Source solidity 0.26 assumes 0.19 m throughout. c/R = 0.076 is nominal (decision 9). Fig 7 repeats earlier runs; Figs 8 and 10 use another normalisation; Figs 11-14 revisit data, model and anemometer comparisons. The two 150-rpm campaigns are distinct and must stay separate.

### Sheldahl1980

Fig 7 (PDF p22): three N=3 curves at 125 / 137.5 / 150 rpm (Re_rot 250000 / 280000 / 300000). Fig 9 (p28): two N=2 curves at 162.5 / 175 rpm (330000 / 356000). NACA0015 throughout; chord 0.1524 m (p12); reported c/R = 0.067 (p33). The reported ratio is kept rather than recomputed from the nominal 5 m diameter (0.1524 / 2.5 = 0.061). Site altitude 1658 m. Figs 8 and 10 are alternative normalisations; Figs 11-13 repeat experimental comparisons or add model results; Fig 14 is drag. Repeated scan pages are not new datasets. The 175 rpm data should be used with reservation (the paper notes induction-motor operation).

## 5. Reynolds-number procedures

| Source | Re_basis | Formula | Notes |
|---|---|---|---|
| Battisti2016 | pointwise from Re_rot | Re_D = 2 Re_rot / (cToR TSR) | cToR = 0.099606; Re_rot 138000 / 205000; each positive TSR |
| Battisti2018 | pointwise from U | Re_D = 1.51 U / 1.5e-5 = 100666.667 U | D = 1.51 m; use each Table 9 wind speed; do not use 174350 as a constant |
| Blackwell1976 C001-C016 | pointwise from Re_rot | Re_D = 2 Re_rot / (cToR TSR) | curve-specific reported Re_c and cToR; each positive TSR |
| Blackwell1976 C017-C026 | estimated | Re_D = 1.9596 U / 1.5e-5 | constant per curve: U 7 / 9 / 11 m/s gives 914480 / 1175760 / 1437040 |
| Muraca1976 | pointwise from U | Re_D = 4.2672 U / 1.5e-5 = 284480 U | use each complete Table I wind speed |
| Sheldahl1977 | pointwise from Re_rot | Re_D = 2 Re_rot / (cToR TSR) | nominal cToR = 0.076; each positive TSR |
| Sheldahl1980 | pointwise from Re_rot | Re_D = 2 Re_rot / (0.067 TSR) | each positive TSR |

Boundaries: the rotational conversion is valid only when Re_rot = omega R c / nu and TSR = omega R / U use matching conventions. A freestream chord Reynolds number instead gives Re_D = 2 Re_c / cToR, with no TSR divisor. Never evaluate at TSR = 0. The fixed-U values are estimates from assumed air, not source-reported diameter Reynolds numbers.

## 6. Open items

- **Battisti2016 geometry** (c, R_eq, hence c/R 0.099606) comes from the companion Energy paper, which is not in this folder.
- **Battisti2016 folder** sits outside `!archive` (moved there by the user); move it in if you want the same layout as the other sources.
- **Source inconsistencies kept, not resolved:** Blackwell Table I versus Fig 10; Muraca imperial-to-metric chord typo; Sheldahl1980 nominal diameter versus reported c/R.
- **Point order:** Blackwell C003, C014, C015, C026 and Muraca are not in TSR order. Muraca follows the paper's table order. Sort a plotting copy only.
- **Leads:** audit Ashwill1992 (Sandia 34-m), WorstellAddendum (Sandia 17-m) and the other leads in `sources.csv` before adding curves.

## 7. Verification log

**2026-11-02 PDF audit.** All 41 metadata rows were compared with the PDFs and figure images.
- **Confirmed:** Battisti2016 rpm, Re_rot, N and Tab 1-4 conditions; Battisti2018 geometry, solidity 0.38, Re_c and spokes; Blackwell Table I chords, radius and all 16 Re legends; Muraca N, D, chord and every Table I value in the CSV; Sheldahl1980 legends, geometry and Fig 7 peaks; Sheldahl1977 Fig 9 legend and Re values.
- **Fixed:** Sheldahl1980 C004/C005 (decision 8); Sheldahl1977 filenames, layout and Re_D method (decision 9); stale sources.csv text.
- **Confirmed by the user:** Blackwell Fig 19 speeds (C025-C026); Sheldahl1977 re-digitization (see decision 12).
- **Not verifiable here:** Battisti2016 geometry (companion paper absent; c and R_eq imply nu of about 1.55e-5 m2/s, plausible); Sheldahl1977 geometry (scan without a text layer; corroborated by Sheldahl1980's description of the original blades).

## 8. Change history

- **2026-11-02 (supporting sources):** The two `Supporting` rows (Battisti2016Energy, VeersCompilation) were removed from `sources.csv` and are named in section 4 and in the Battisti2016 notes instead. The workbook in this folder is named `metadata_troposkein.xlsx`; the tool accepts any single `metadata*.xlsx`.
- **2026-11-02 (Battisti2016):** Tab 1-4 extracted into four workbooks and four CSVs (decision 13); the four rows changed from `Extract` to `Use`. Troposkein now has 41 curves, all done, none to check or pending.
- **2026-11-02 (Sheldahl1977 / Blackwell):** Blackwell C025-C026 confirmed; Sheldahl1977 re-digitized by the user, files C002/C003 exchanged and all four reformatted (decision 12). Troposkein now has 37 done, 0 to check, 4 pending (the Battisti2016 tables).
- **2026-11-02 (later):** `metadata.csv` deleted; `metadata.xlsx` is now the only metadata store and `tools/vawt_management.py refresh` replaces `build`. One blank row now separates sources inside the Metadata sheet. Highlight colour for rows needing a check is yellow. Each yellow row's Notes now carry a "Check: ... To do: ..." sentence, collected on the new "To check" sheet. No curves were removed here: the four pending Battisti2016 rows are the only primary Tab 1-4 data, so they are not duplicates.

- **2026-11-02:** Management folder standardized with the default folder. Files renamed to `metadata.csv`, `sources.csv`, `ASSUMPTIONS_AND_CHANGES.md`; `rename_map` retired; `metadata.xlsx` and `tools/vawt_management.py` added. Action values replaced (`Use with nominal equatorial geometry` -> `Use - check`; the four Battisti2016 rows -> `Extract`); Re_basis changed from formula strings to the shared vocabulary (formulas remain in Notes); `assumed_mu` / `assumed_rho` blanked on 16 Blackwell rows that do not use them; mu written as 1.80E-05; foil names written as `NACA0012`. Sheldahl1980 swap and Sheldahl1977 rename recorded in decisions 8-9. Battisti2016 and Sheldahl1977 moved into `!archive/` so all six sources share one layout (Battisti2016 has no `data/` folder yet).
- **2026-10-24:** Metadata re-audit and source spacing: one empty separator row between sources; Battisti2018 Struts set to "no" (blade-support spokes, not shaft or hub); numerical checks of c/R for Battisti2018, Blackwell, Muraca and Sheldahl1980; source-specific Reynolds instructions added to Notes and to the sources audit notes; known source issues documented.
- **Earlier:** Initial troposkein set built from six PDFs with 41 planned curves; IDs restarted per source; unknown c/R handling defined.
