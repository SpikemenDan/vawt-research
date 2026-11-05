# Default VAWT: management log

Straight-bladed (H-type) and other non-troposkien rotors. Last updated 2026-11-05.

## 1. Files in this folder

| File | Purpose |
|---|---|
| `metadata.xlsx` | One row per retained experimental curve (178: 110 done, 68 pending). The only metadata store; there is no metadata CSV. Green = done, yellow = needs a check (the "To check" sheet says what to do), no fill = pending. One blank row separates sources. After editing the Metadata sheet, run `python tools/vawt_management.py refresh "(Default) Research Papers"` to recompute status and colours. |
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
- **Assumed water:** mu = 1.00E-03 Pa s, rho = 1000 kg/m3, so nu = 1.00E-06 m2/s (decision 16).
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
10. **Duplicates and skipped figures (2026-11-02):** Howell Figs 10 and 11 (experimental markers at 4.31 and 5.07 m/s) repeat the 3-blade curves in Fig 8; Li Fig 12 replots the optimum-pitch curves of Fig 11 (N=2 beta 6, N=3 beta 8, N=4 beta 8, N=5 beta 12 = C002, C005, C008, C011); Li Fig 21 replots the two-bladed wind-tunnel measurements for a CFD comparison. Howell Fig 12 (5.81 m/s, five points, blade finish not stated) is not a repeat but was deliberately skipped. These eight rows were deleted from the metadata. To add Fig 12 later, append a Howell2010-C017 row and extract the circles.
11. **Importer:** the current importer requires U_m_s. Where it is unknown, leave it blank and resolve the importer handling rather than inventing a value. Group curves by all differing conditions, not only N and cToR.
12. **`TurbineResearch/unh_data` is RM2, not UNH-RVAT (2026-11-05, not yet fixed).** The five `Perf-*.csv` files run TSR 1.0-5.75 in 0.25 steps and peak at Cp 0.156 / 0.285 / 0.341 / 0.355 / 0.370 at TSR 3.4 / 3.3 / 3.1 / 3.1 / 3.1. That matches RM2 (Bachant et al. 2016, `Perf-{speed}` run sets, lambda 3.1) and not UNH-RVAT (Bachant and Wosnik 2016, TSR 0.1-3.1 in 0.1 steps, peak near 1.9-2.0). Both studies towed at 0.4-1.2 m/s, which is probably how they were confused. The notebook sets `cToR = 0.14 / 0.5` and calls the set UNH-RVAT, so these points carry c/R 0.28 instead of about 0.10, and every solidity and Dynamic_Flow_Opacity value derived from it is wrong by a factor of 2.8. Confirmed directly: the public RM2 `Perf-1.0.csv` has the same 23 rows and first-row values as ours, while the public RVAT file has 31 rows and peaks at Cp 0.262, TSR 1.90 (only this file was compared row by row). Reach: 125 of 4,298 rows in `master_raw_matrix.parquet`, 5 of 234 in `master_peak_matrix.parquet`, and notebook Actions 1 and 2, which use `Dynamic_Flow_Opacity`. `df_compute.csv` is clean (4,083 rows, none at c/R 0.28). The `.pkl` models could not be opened here, and the Default notebook does not train them, so they are unconfirmed; this replaces the earlier statement that anything fitted needs rerunning. Fix on hold at the user's request pending post-doc review; explainer in `UNH_RM2_Data_Mislabel.html` in this folder. No notebook, parquet or model file was edited.
13. **Literature list (2026-11-05).** The list is Table 1 of Hunt et al. 2024 (Renew. Sustain. Energy Rev. 206, 114848; arXiv 2310.20616), and the bracketed numbers are that paper's references. The CSV export lost the hyperlinks, so the Link column holds only page titles; each paper was re-identified from Hunt's reference list. Hunt states five entries use curved blades, so those were routed to the Troposkein folder, not here. Hunt's values are recorded in `sources.csv` as secondary until a paper is read.
14. **Takamatsu confinement.** The 1985 rotors run in a closed channel with S/D 0.95-1.33 (D/S up to about 1), which is ducted flow, not an open stream with blockage. Standard open-flow blockage corrections are not valid at this ratio, so the literature list's blockage note cannot be met by a routine correction. Cp is stored uncorrected on swept area. Decide whether these curves belong in the same analysis before use.
15. **Efficiency is not Cp.** Takamatsu's efficiency is shaft power over hydraulic power from measured head. Takamatsu1985a is converted from the torque coefficient (Cp = 2 (U/V) Ct) and Takamatsu1985b has a measured Cp series. Takamatsu1991 reports only eta_b, so it has no metadata rows and stays on Hold. The same check applies to Shiono2000.
16. **Assumed water** (mu 1.00E-03 Pa s, rho 1000 kg/m3) is new and matches Hunt's nu = 1.0E-06 m2/s. Used for Bachant2016RM2, BachantWosnik2016 and Takamatsu1985a. Araya2017 uses its reported Re_D. Re_D for the Tanino and Szczerba rows uses the standard assumed air, so values differ slightly from Hunt (nu 1.6E-05).
17. **Repeats not added:** Miller2021 N=5 repeats Miller2018; Li2016 probably repeats the Li2015 Fig 12 optimum-pitch curves; Tanino Fig 10 NACA series should repeat Figs 4-5.

## 4. Source status

| Source | Curves | CSVs | Status |
|---|---|---|---|
| Eboibi2016 | 6 | 6 | Done |
| ElSamanoudy2010 | 25 | 25 | Done |
| Howell2010 | 16 | 16 | Done; Figs 10-11 repeat Fig 8; Fig 12 skipped |
| Li2015 | 12 | 12 | Done; Figs 12 and 21 repeat Fig 11 |
| Migliore1980 | 2 | 2 | Done |
| Miller2018 | 22 | 22 | Done |
| SomoanoHueraHuarte2018 | 27 | 27 | Done |
| Araya2017 | 3 | 0 | Pending; Fig 5 capture |
| Bachant2016RM2 | 6 | 0 | Pending; numeric data, see decision 12 |
| BachantWosnik2016 | 5 | 0 | Pending; numeric data |
| Szczerba2023 | 30 | 0 | Pending; Figs 10-14 capture |
| Takamatsu1985a | 6 | 0 | Pending; Fig 5 capture, Cp from Ct |
| Takamatsu1985b | 3 | 0 | Pending; Fig 10 capture |
| Tanino2011 | 15 | 0 | Pending; Figs 4, 5, 10 capture |
| **Total** | **178** | **110** | 110 done, 0 to check, 68 pending |

Twelve more sources are in `sources.csv` with no curves yet, because their figures have not been seen: Armstrong2012, Du2019, FiedlerTullis2009, Lam2018, Li2016, McAdam2013, Miller2021, PriegueStoesser2017, RossPolagye2022, Shiono2000, Takamatsu1991 (Hold, no Cp), Zhao2013.

### Literature list audit (2026-11-05)

Every row of `Literature List Experimental Work(Sheet1).csv`, in list order.

| List row | Ref | Result |
|---|---|---|
| Blackwell and Sheldahl 1977 | [36] | Troposkein. Journal summary of Blackwell1976; no new curves expected |
| Sheldahl et al. 1980 | [37] | Troposkein. Already done as Sheldahl1980 |
| Migliore et al. 1980 | [4], [38] | Done as Migliore1980 ([4]). Report [38] not audited |
| Klimas and Worstell 1981 | [18] | Troposkein. KlimasWorstell1981, PDF needed |
| Worstell 1981 | [39] | Troposkein. Worstell1981, PDF needed |
| Takamatsu et al. 1985 | [23] | Takamatsu1985b, 3 curves |
| Takamatsu et al. 1985 | [19] | Takamatsu1985a, 6 curves |
| Takamatsu et al. 1991 | [40] | Takamatsu1991, Hold: efficiency only |
| Ashwill 1992 | [41] | Troposkein. Ashwill1992, PDF needed |
| Shiono et al. 2000 | [42] | Shiono2000, PDF needed |
| Fiedler and Tullis 2009 | [20] | FiedlerTullis2009, PDF needed |
| Howell et al. 2010 | [32] | Done as Howell2010 |
| El-Samanoudy et al. 2010 | [43] | Done as ElSamanoudy2010 |
| Tanino et al. 2011 | [44] | Tanino2011, 15 curves |
| Armstrong et al. 2012 | [29] | Armstrong2012, PDF needed |
| McAdam et al. 2013 | [13], [14] | McAdam2013, both PDFs needed |
| Zhao et al. 2013 | [21] | Zhao2013, PDF needed |
| Li et al. 2015 | [15] | Done as Li2015 |
| Bachant and Wosnik 2016 | [11] | BachantWosnik2016, 5 curves. Not in repo (decision 12) |
| Eboibi et al. 2016 | [45] | Done as Eboibi2016 |
| Li et al. 2016 | [46] | Li2016, Hold: probable repeat, PDF needed |
| Bachant et al. 2016 | [47] | Bachant2016RM2, 6 curves. In repo under the wrong name (decision 12) |
| Priegue and Stoesser 2017 | [33] | PriegueStoesser2017, PDF needed |
| Araya et al. 2017 | [16] | Araya2017, 3 curves |
| Miller et al. 2018 | [12] | Done as Miller2018 |
| Lam et al. 2018 | [48] | Lam2018, PDF needed |
| Somoano and Huera-Huarte 2018 | [49] | Done as SomoanoHueraHuarte2018 |
| Du et al. 2019 | [27] | Du2019, open-access PDF needed |
| Miller et al. 2021 | [17] | Miller2021, PDF needed for curve count; N=5 repeats Miller2018 |
| Ross and Polagye 2022 | [50] | RossPolagye2022, PDF needed; dataset exists |
| Szczerba et al. 2023 | [51] | Szczerba2023, 30 curves |

**Hunt Table 1 versus this folder:** Li2015 pitch is -10 to 4 deg in Hunt but beta 4-14 deg in the paper's Fig 11; the paper governs and the metadata match it. Miller2018 is 5-50e5 in Hunt, matching the paper's stated test range, while Figs 3-4 here cover 0.89-3.96e6; the rest is in the Fig 5 scatter not imported. All other done sources agree within rounding and Hunt's nu.


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

- **UNH data (decision 12):** relabel as RM2 with c/R 0.1 in the notebook, then rerun what depends on it. Download the real UNH-RVAT data if wanted.
- **Takamatsu (decisions 14-15):** decide whether ducted runners belong in the analysis, and whether Takamatsu1991 efficiency is wanted at all.
- **Tanino Table 2:** base size prints 10 m/s, but Re 1.5e4 implies about 8 m/s (Hunt's Re_D range also implies 8 m/s).
- **Takamatsu1985b:** U and Re_D are blank for Fig 10, and pp1125-1127 were not read. **Takamatsu1985a** p1096 was not read.
- **Migliore report** ORO-5135-77/7 (open OSTI scan, 116 pages): check for Cp curves beyond the journal's Fig 11.
- **Hunt 2024 dataset** feeds the notebook but has no row in `sources.csv`.
- **Dummy rows:** `master_raw_matrix.parquet` holds 90 rows labelled dummy / dummy5 (6 in the peak matrix). Remove them if they are leftover test uploads.
- **Li:** check the Fig 11d peak markers and the small negative endpoint of Fig 11b pitch 6.
- **Yellow rows:** none. Anything that needs checking appears on the "To check" sheet of `metadata.xlsx`.
- **Miller:** Fig 5 field data would need separate provenance and per-point Re if ever collected.
- **Somoano:** near-zero cases may overlap; do not invent separate points where symbols cannot be told apart.
- **Point order:** 20 data files are not in TSR order (El-Samanoudy Fig 6 pitch 20, Howell Figs 7-8, Migliore c/R 0.114, Miller Figs 3b and 4b, Somoano Figs 4-6). Sort a plotting copy, not the original. Migliore's last c/R 0.114 point may follow a curve extension rather than a symbol.
- **Small curves:** several El-Samanoudy curves have only 2-5 points and overlap near the origin; check curve identity and peak accuracy by eye.
## 6. Verification log

**2026-11-02 PDF audit.** All 118 metadata rows were compared with the seven PDFs and their figure screenshots (blade count, radius, chord, c/R, airfoil, wind speeds, pitch and pressure legends, Re values). All matched; the Miller Fig 3b pressures could not be read from the text and were confirmed against the Fig 3a legend by the user. Howell's strut loss is left blank although its spin-down tests removed the blades and kept the spokes. Li2015 digitized peaks (0.195 for N=3, beta 8) agree with the reported 0.189.

**2026-11-05 literature list audit.** All 31 list rows were identified against Hunt et al. 2024. Papers read directly: Araya2017 (PDF text), Bachant2016RM2 and BachantWosnik2016 (article text), Szczerba2023 (article text and Figs 10-14), Takamatsu1985a and 1985b (page images, partial), Takamatsu1991 (all page images), Tanino2011 (PDF), Miller2021 (article text only). No data CSV was created and no figure was captured. The 110 existing rows are unchanged, confirmed against the last commit.

## 7. Change history

- **2026-11-05 (literature list):** Added 19 sources and 68 pending curves from the Hunt Table 1 list (decisions 12-17). Migliore1980 audit note extended. The `estimated` Re_basis text now says assumed fluid, not air, because water rows use it. Default now has 178 curves: 110 done, 0 to check, 68 pending.
- **2026-11-02 (Howell Fig 12):** Skipped by the user; row Howell2010-C017 deleted. Default now has 110 curves, all done, none to check or pending.
- **2026-11-02 (Miller):** Fig 3b pressures (125/156/183/203 bar) confirmed against the Fig 3a legend by the user. Miller2018 C001-C004 changed from `Use - check` to `Use` (green); Default now has 110 done, 0 to check, 1 pending.
- **2026-11-02 (data files):** Added the missing `cToR` column (0.265) to the 12 Li2015 Fig 11 files and the missing `Re_D` column (426667) to ElSamanoudy2010-C001, so all 110 data files now carry `cToR` and `Re_D`; no TSR or Cp value changed. Renamed the 18 Howell, Miller, Somoano and Migliore screenshots to `SourceYear (Fig X).png` like the others. Deleted the stale `(Default) Research Papers.zip` snapshot.
- **2026-11-02 (later):** `metadata.csv` deleted; `metadata.xlsx` is the only metadata store and `tools/vawt_management.py refresh` replaces `build`. One blank row now separates sources. Seven duplicate rows (Howell C017-C018, Li C013-C017) removed and Howell Fig 12 renumbered C019 -> C017 (decision 10); the curve count is 111. Rows needing a check are yellow, and each carries a "Check: ... To do: ..." note collected on the "To check" sheet.
- **2026-11-02:** Management folder standardized with the troposkein folder. Blank row after the header removed; BOM removed. Action vocabulary replaced (`Digitize` -> `Use` for the 61 extracted curves, `Extract` for the one pending); four Miller Fig 3b rows set to `Use - check`. Added `sources.csv`, `metadata.xlsx` and the shared tooling in `tools/`.
- **2026-09-28 (second change):** Removed nine repeated El-Samanoudy entries and reassigned IDs consecutively per source (see decision 2). Old IDs may now belong to different curves; match full filenames, not the number alone. 118 curve rows remain.
- **2026-09-28 (first change):** Tables sorted alphabetically by source and numerically by figure (panels 11a-11d included); within a figure by N, c/R, velocity, pitch, pressure, surface and foil. IDs were reassigned once at the user's request to follow that order.
