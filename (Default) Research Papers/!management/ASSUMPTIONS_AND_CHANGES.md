# Default VAWT: management log

Straight-bladed (H-type) and other non-troposkien rotors. Last updated 2026-11-02.

## 1. Files in this folder

| File | Purpose |
|---|---|
| `metadata.xlsx` | One row per retained experimental curve (111). The only metadata store; there is no metadata CSV. Green = done, yellow = needs a check (the "To check" sheet says what to do), no fill = pending. One blank row separates sources. After editing the Metadata sheet, run `python tools/vawt_management.py refresh "(Default) Research Papers"` to recompute status and colours. |
| `sources.csv` | One row per paper: citation, rotor, what was extracted, audit notes, DOI link. |
| `ASSUMPTIONS_AND_CHANGES.md` | This log. |

The old `rename_map.csv` and its `.xlsx` were retired on 2026-11-02. They only mapped the original upload names to the short names, which are now final; `metadata.xlsx` carries the filename for every curve.

## 2. Conventions

- **Filename:** `SourceYear (Fig 4) (N = 3) (cToR = 0.085714) (C001).csv`. Panel suffixes are kept (`Fig 11a`). Numerical tables use `Tab` instead of `Fig`.
- **Curve_ID:** `SourceYear-C001`. C-numbers are unique within a source, restart at C001 for each source, and carry no physics. Keep assigned IDs when adding curves.
- **Match metadata to a data file** by filename or Curve_ID. Copy the constants you need into the data CSV and fill them down every row. TSR and Cp are the varying columns.
- **Blank means unknown or not assigned, never zero.**
- **Action** (documentation only): `Use` = CSV exists and metadata checked against the paper; `Use - check` = CSV exists but a known issue needs review; `Extract`, `Capture figure`, `Review repeat` = not extracted yet.
- **Re_basis:** `reported`, `reported approximate`, `estimated`, `estimated from peak TSR and reported Re_rot`. Definitions are on the Legend sheet of the workbook.
- **Assumed air:** mu = 1.80E-05 Pa s, rho = 1.20 kg/m3, so nu = 1.50E-05 m2/s. The two columns are filled only on rows where the assumption was used.
- **Solidity** is not stored. Nc/R = N(c/R); Nc/D = N(c/R)/2; Nc/(2piR) = N(c/R)/(2pi). The notebook uses the last convention; papers may use another.

## 3. Decisions and assumptions

1. **El-Samanoudy Fig 11:** pitch alpha_p = 0 deg, following the caption and the paper's pattern, although the plot annotation says 10 deg. Approved by the user. N=2 and N=3 stay in the analysis.
2. **El-Samanoudy repeated baselines:** Figs 6 and 7 are the primary sources. Nine repeat curves were removed at the user's request: Fig 10 N4; Fig 11 N4; Fig 14 c/R 0.375; Figs 16 and 17 NACA0024 and NACA4420; Figs 20 and 21 c/R 0.375. 25 El-Samanoudy curves remain. PDFs and screenshots are kept because those figures also hold distinct curves.
3. **El-Samanoudy Fig 20, c/R 0.30:** original row 1 (TSR = -0.03339906716055985, Cp = -0.0009961583318073286) removed as a suspected digitization or calibration error; 18 rows became 17. Not a proven physical diagnosis.
4. **Migliore:** Re_D = 2 Re_rot / [TSR_peak (c/R)]. For c/R 0.114: Re_rot 131000, TSR_peak 4.595228782148789, Cp_peak 0.3763607082828982 gives Re_D 500137.3649 (labelled 500137). For c/R 0.260: Re_rot 225000, TSR_peak 2.7211301257167575, Cp_peak 0.14002665531085196 gives 636047.9473 (labelled 636048). These are estimates at the digitized peak; one Re_D over a whole curve would need constant freestream speed and fluid properties, which is not established. No viscosity is needed. Re_rot is preserved in the metadata.
5. **Nominal air estimates** for Eboibi, Li, Howell and El-Samanoudy: Re_D = rho U (2R) / mu with the assumed air above. These are assumptions, not measured conditions. Integer-looking labels do not imply integer precision. Eboibi's own Re (16,800-84,000) is chord-scale and is not used.
6. **Miller:** use the reported Re_D for compressed air, not an ambient-air value. Different pressures are distinct runs even where curves collapse. The custom WPE profile resembles NACA0021 but is not labelled exactly NACA0021.
7. **Somoano:** air, reported approximate Re_D 300000/400000/500000. Pitch magnitude and toe-in/toe-out direction are stored separately; no cross-paper sign convention is imposed. Physical struts and the strut-drag correction are separate properties.
8. **Migliore publication year** is 1980, not 2012 as in the old PDF filename.
9. **El-Samanoudy Cp values are already fractions.** Do not divide by 100 again.
10. **Duplicates not collected (2026-11-02):** Howell Figs 10 and 11 (experimental markers at 4.31 and 5.07 m/s) repeat the 3-blade curves in Fig 8; Li Fig 12 replots the optimum-pitch curves of Fig 11 (N=2 beta 6, N=3 beta 8, N=4 beta 8, N=5 beta 12 = C002, C005, C008, C011); Li Fig 21 replots the two-bladed wind-tunnel measurements for a CFD comparison. These seven rows were deleted from the metadata and the IDs renumbered (Howell Fig 12 became C017). Howell Fig 12 (5.81 m/s) is not a repeat, because no collected curve has that speed, so it stays pending.
11. **Importer:** the current importer requires U_m_s. Where it is unknown, leave it blank and resolve the importer handling rather than inventing a value. Group curves by all differing conditions, not only N and cToR.

## 4. Source status

| Source | Curves | CSVs | Status |
|---|---|---|---|
| Eboibi2016 | 6 | 6 | Done |
| ElSamanoudy2010 | 25 | 25 | Done |
| Howell2010 | 17 | 16 | Figs 7-8 done; Fig 12 (5.81 m/s) pending; Figs 10-11 repeat Fig 8 |
| Li2015 | 12 | 12 | Done; Figs 12 and 21 repeat Fig 11 |
| Migliore1980 | 2 | 2 | Done |
| Miller2018 | 22 | 22 | Done; Fig 3b flagged |
| SomoanoHueraHuarte2018 | 27 | 27 | Done |
| **Total** | **111** | **110** | 106 done, 4 to check, 1 pending |

### Missing-figure check

| Source | Result |
|---|---|
| Eboibi2016 | Core complete. Fig 6 repeats a comparison and is not a new case. |
| ElSamanoudy2010 | Core figures saved. Fig 24 compares the paper's own baseline; Hwang curves need the original source. Fig 7 has seven cases (no 60 deg). |
| Howell2010 | Direct Cp-TSR figures saved; experimental markers only, all CFD excluded. |
| Li2015 | Fig 11 complete. Figs 12 and 21 repeat Fig 11 data and were not collected. |
| Migliore1980 | Experimental Fig 11 complete. |
| Miller2018 | Direct plots saved. Fig 5 field scatter and Fig 9 derived mean are not primary runs. |
| SomoanoHueraHuarte2018 | Core Figs 4-6 complete; the other saved plots are methods or comparisons. |

## 5. Open items

- **Howell:** extract the Fig 12 experimental circles (C017, 5.81 m/s, five points); this is the only new run left. If you decide it is not worth collecting, delete the row.
- **Li:** check the Fig 11d peak markers and the small negative endpoint of Fig 11b pitch 6.
- **Yellow rows** (Miller2018 C001-C004, Fig 3b) are listed with instructions on the "To check" sheet of `metadata.xlsx`.
- **Miller:** Fig 3b pressure values (125/156/183/203 bar) could not be machine-verified; the caption confirms four pressures. Fig 5 field data would need separate provenance and per-point Re.
- **Somoano:** near-zero cases may overlap; do not invent separate points where symbols cannot be told apart.
- **Point order:** 20 data files are not in TSR order (El-Samanoudy Fig 6 pitch 20, Howell Figs 7-8, Migliore c/R 0.114, Miller Figs 3b and 4b, Somoano Figs 4-6). Sort a plotting copy, not the original. Migliore's last c/R 0.114 point may follow a curve extension rather than a symbol.
- **Small curves:** several El-Samanoudy curves have only 2-5 points and overlap near the origin; check curve identity and peak accuracy by eye.
## 6. Verification log

**2026-11-02 PDF audit.** All 118 metadata rows were compared with the seven PDFs and their figure screenshots (blade count, radius, chord, c/R, airfoil, wind speeds, pitch and pressure legends, Re values). All matched, with these limits: Miller Fig 3b pressure values are unverified (see section 5), and Howell's strut loss is left blank although its spin-down tests removed the blades and kept the spokes. Li2015 digitized peaks (0.195 for N=3, beta 8) agree with the reported 0.189.

## 7. Change history

- **2026-11-02 (data files):** Added the missing `cToR` column (0.265) to the 12 Li2015 Fig 11 files and the missing `Re_D` column (426667) to ElSamanoudy2010-C001, so all 110 data files now carry `cToR` and `Re_D`; no TSR or Cp value changed. Renamed the 18 Howell, Miller, Somoano and Migliore screenshots to `SourceYear (Fig X).png` like the others. Deleted the stale `(Default) Research Papers.zip` snapshot.
- **2026-11-02 (later):** `metadata.csv` deleted; `metadata.xlsx` is the only metadata store and `tools/vawt_management.py refresh` replaces `build`. One blank row now separates sources. Seven duplicate rows (Howell C017-C018, Li C013-C017) removed and Howell Fig 12 renumbered C019 -> C017 (decision 10); the curve count is 111. Rows needing a check are yellow, and each carries a "Check: ... To do: ..." note collected on the "To check" sheet.
- **2026-11-02:** Management folder standardized with the troposkein folder. Blank row after the header removed; BOM removed. Action vocabulary replaced (`Digitize` -> `Use` for the 61 extracted curves, `Extract` for the one pending); four Miller Fig 3b rows set to `Use - check`. Added `sources.csv`, `metadata.xlsx` and the shared tooling in `tools/`.
- **2026-09-28 (second change):** Removed nine repeated El-Samanoudy entries and reassigned IDs consecutively per source (see decision 2). Old IDs may now belong to different curves; match full filenames, not the number alone. 118 curve rows remain.
- **2026-09-28 (first change):** Tables sorted alphabetically by source and numerically by figure (panels 11a-11d included); within a figure by N, c/R, velocity, pitch, pressure, surface and foil. IDs were reassigned once at the user's request to follow that order.
