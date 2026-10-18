# Short filenames, metadata, and decisions

## Use these two tables

- rename_map.csv: original relative path, previous proposed filename, newly sorted filename, Curve_ID and action. Includes 87 existing research assets after removal of nine reference-only CSV entries, plus 73 planned curve files. “Not created yet” means a filename suggestion, not a completed CSV.
- metadata.csv: one row per retained curve (45 existing + 73 planned). Match by filename. Copy the needed column headings and values into the experimental CSV and fill the same constants down every data row. Blank means unknown/not assigned, never zero. Keep TSR and Cp as your varying measurement columns. Action and Notes are documentation, not numerical model inputs.

Example: SourceYear (Fig 4) (N = 3) (cToR = 0.085714) (C001).csv
The C-number is only a unique curve identifier within a source. Use the table to see its conditions. It does not encode physics and is not an experimental run number. Preserve these assigned IDs when adding future curves. No optional conditions need to be typed into filenames.

Filenames are verified shorter than 259 characters. A long parent folder can still make the full Windows path too long; keep the project folder short, such as C:\Research. This package contains no automatic renaming script and does not alter your originals.

## Decisions and assumptions

1. El-Samanoudy Fig11: user approved alpha_p=0 degrees, following caption and paper pattern. Plot annotation still says10 degrees; assumption retained explicitly. N2 and N3 remain in analysis; N4 is a reference-only repeat.
2. Repeated El-Samanoudy baselines: retain Figs6 and7 as primary sources. Nine other CSV copies have been removed from the working tables at the user’s request: Fig10 N4; Fig11 N4 under the zero-pitch assumption; Fig14 c/R0.375; Fig16 NACA0024 and4420; Fig17 NACA0024 and4420; Fig20 c/R0.375; Fig21 c/R0.375. Keep the other distinct curves. This leaves25 El-Samanoudy curves for analysis. The user intends to delete these redundant CSV copies locally; the original uploaded ZIP remains unchanged.
3. El-Samanoudy Fig20 c/R0.30: user approved removal of original row1, TSR=-0.03339906716055985 and Cp=-0.0009961583318073286. 18 rows become17; all other rows unchanged. Use the corrected CSV supplied separately in ElSamanoudy_Fig20_cToR030_Corrected.zip. Suspected digitization/calibration error, not a proven physical diagnosis. Do not use the uncorrected version from the original upload.
4. Migliore conversion approved: Re_D=2 Re_rot/[TSR_peak (c/R)]. For c/R0.114, Re_rot131000, TSR_peak4.595228782148789, Cp_peak0.3763607082828982 gives Re_D500137.3649 (label500137). For c/R0.260, Re_rot225000, TSR_peak2.7211301257167575, Cp_peak0.14002665531085196 gives Re_D636047.9473 (label636048). These are estimates at peak Cp using digitized peaks. Using a single Re_D over a complete curve requires constant freestream velocity and fluid properties; that condition is not established here. Do not interpret the reference Re_rot as constant at every TSR. No viscosity assumption is needed for the conversion. Original Re_rot is preserved in metadata.
5. Nominal air estimates for Eboibi, Li, Howell and El-Samanoudy: assumed dynamic viscosity mu=1.80e-5 Pa s and density rho=1.20 kg/m3; nu=mu/rho=1.50e-5 m2/s. Re_D=rho U(2R)/mu. These are assumptions, not measured conditions. Both assumed properties are explicit table columns. Estimated integer labels do not imply integer-level physical precision.
6. Miller: use reported Re_D for compressed-air conditions, not ambient-air density. Different pressures are distinct runs even where curves collapse. Custom profile resembles NACA0021 but is not labeled exactly NACA0021.
7. Somoano: air, reported approximate Re_D300000/400000/500000. Pitch magnitude and toe-in/toe-out direction kept separate; no unapproved cross-paper sign convention. Physical struts and removal of strut-drag losses are separate properties.
8. Solidity is not added as an ambiguous constant: Nc/R=N(c/R); Nc/D=N(c/R)/2; Nc/(2piR)=N(c/R)/(2pi). Your code uses the last convention. Papers may use another.
9. Migliore publication year1980, not2012 in the old PDF filename. El-Samanoudy CSV Cp values already are fractions, so do NOT divide by100 again.

## What still needs review

- Howell Figs7-8:16 distinct rough/smooth and speed cases. Fig12 experimental circles:one additional extraction. Figs10-11 experimental circles may repeat Fig8; compare before counting. Exclude all CFD series. Fig7/8 U5.45 differs from Fig12 U5.81.
- Li: capture Fig12 (PDF p.8), four optimum-pitch curves, and Fig21 (PDF p.11), black experimental series only. Compare with Fig11 before adding as independent runs. Fig21 pitch remains unverified. Check Fig11d peak markers and the small negative endpoint of11b pitch6.
- Miller:22 pressure-specific cases in Figs3b and4a-f. Fig5 field scatter needs separate provenance and per-point Re handling; tunnel repeats must not be counted twice. Fig9 is a derived mean, not another primary run.
- Somoano:27 cases in Figs4-6. Near-zero cases may overlap; do not invent separate points where symbols cannot be distinguished. Fig3 left repeats8-degree toe-out cases; right is not Cp-TSR. Fig2d is a method example, not an identified additional run.
- Existing unsorted points: El-Samanoudy Fig10 N4 (reference only), Fig6 pitch20, and Migliore c/R0.114. Order should be checked before sorting a plotting copy. No sorting performed here. Migliore's last c/R0.114 point may follow a curve extension rather than a measured symbol.
- Several small El-Samanoudy curves have only2-5 points and overlap near the origin; curve identity/peak accuracy needs visual checking. No automatic correction made.

## Missing figure check

| Source | Result |
|---|---|
| Eboibi2016 | Core complete. Missing Fig6 screenshot is a repeated comparison, not a new primary case. |
| ElSamanoudy2010 | Core figures saved. Fig24 missing comparison: own baseline repeats; Hwang curves require the original source for verification. Fig7 has seven cases, no60-degree case. |
| Howell2010 | All direct Cp-TSR figures saved; experimental curves only. |
| Li2015 | Figs12 and21 missing as screenshots; capture and reconcile as above. |
| Migliore1980 | Experimental Fig11 complete. |
| Miller2018 | Direct plots saved; distinguish pressure runs, field scatter and derived mean. |
| SomoanoHueraHuarte2018 | Core Figs4-6 complete; other saved plots are methods/comparisons. |

## Standing workflow

For each new paper: verify actual experimental Cp-TSR curves and repeated baselines BEFORE requesting digitization; audit geometry, conditions and CSV values; identify missing figures; ask about unresolved decisions one at a time in chat. Record user decisions, assumptions, units, equations, source conflicts and edits here. Return only a rename map, a curve metadata table, and this readable log; no redundant audit CSVs. Original research files remain intact.

Renaming is not metadata ingestion. Your current importer requires U_m_s; if unknown, leave it unknown and resolve importer handling rather than inventing a value. After manually adding metadata, group curves by all relevant differing conditions, not only N and cToR. No notebook changes are included.

## User-requested alphabetical/numerical ordering — 2026-09-28

Both CSV tables are now sorted alphabetically by source and numerically by figure (including panel suffixes: 11a,11b,11c,11d). Within a figure, curve order uses N, c/R, velocity, pitch magnitude/direction, pressure, surface and foil. PDF references come first within each source, and screenshots precede curve entries for the same figure.

C identifiers were deliberately reassigned once, at the user’s request, to follow this ordering. They restart at C001 for each source, including existing and planned curves. The full Curve_ID (SourceYear-Cxxx) is the matching key in both tables; non-curve assets have a blank Curve_ID. previous_filename in rename_map records the former proposed name so already-renamed files can be matched. current_file still records the original uploaded path. No measurements, assumptions, or decisions changed during sorting. Use these new IDs in place of the earlier set. Real source CSV/PNG/PDF files were not renamed on the user’s PC.

## Reference-only removal and ID reassignment — 2026-09-28

User requested removal of the nine repeated El-Samanoudy CSV entries from both tables and consecutive ID reassignment. Tables now contain118 curve rows in metadata and160 asset/planned-file rows in rename_map. Remaining curves stay in source/figure order. IDs restart at C001 per source without gaps. previous_filename now records the immediately preceding proposed filename; current_file retains the original uploaded relative path. Use the NEW IDs from this version. No measurement values changed.

Removed entries, identified using their OLD IDs and filenames (these old IDs may now be reused for different retained curves; match full filenames, not the number alone):

- ElSamanoudy2010 (Fig 10) (N = 4) (cToR = 0.375) (C017).csv
- ElSamanoudy2010 (Fig 11) (N = 4) (cToR = 0.375) (C020).csv
- ElSamanoudy2010 (Fig 14) (N = 4) (cToR = 0.375) (C021).csv
- ElSamanoudy2010 (Fig 16) (N = 4) (cToR = 0.375) (C023).csv
- ElSamanoudy2010 (Fig 16) (N = 4) (cToR = 0.375) (C024).csv
- ElSamanoudy2010 (Fig 17) (N = 4) (cToR = 0.375) (C026).csv
- ElSamanoudy2010 (Fig 17) (N = 4) (cToR = 0.375) (C027).csv
- ElSamanoudy2010 (Fig 20) (N = 4) (cToR = 0.375) (C031).csv
- ElSamanoudy2010 (Fig 21) (N = 4) (cToR = 0.375) (C034).csv

Only duplicate curve CSV entries were removed. Keep the source PDFs and figure screenshots: those figures also contain distinct curves still used in analysis. Files on the user’s PC have not been deleted or renamed by this operation.
