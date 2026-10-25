# Troposkein: short filenames, metadata, and decisions

## Use these two tables

- metadata_troposkein.csv: one row per retained experimental curve, using exactly the default metadata columns and their order.
- rename_map_troposkein.csv: the default five columns; includes six supplied PDFs and 41 planned curve CSVs. No screenshots or extracted performance CSVs were supplied for this six-paper set. “Not created yet” is literal; these rows are extraction targets.

Filename: `SourceYear (Fig 4) (N = 3) (cToR = 0.085714) (C001).csv`. Numerical-table filenames use your supplied `Tab` abbreviation instead of `Fig`.

Curve_ID is `SourceYear-C001`. C-numbers restart at C001 for each source. These replace the earlier globally numbered troposkein IDs. `previous_filename` records that earlier proposal; `current_file` is either the actual supplied PDF name or “Not created yet”. IDs are now assigned in source/figure/condition order. Preserve them when adding future data.

Unknown c/R appears as `cToR = unknown` in the proposed filename and remains blank in numerical metadata. Resolve it before geometry-dependent ingestion; do not treat “unknown” as a number. Known c/R is rounded to six decimals to match the default naming style; source dimensions are retained in Notes.

Match metadata by filename or full Curve_ID. Copy appropriate numerical constants into the performance CSV; TSR and Cp are the varying measurement columns. Do not copy a pointwise Reynolds formula as a constant. Action and Notes are documentation. Optional information, including rpm, tilt and provenance, is in Notes to preserve your exact column template.

## Actions

- **Use:** retain this experimental series and extract it; does not mean its CSV already exists or that digitized values have been validated.
- **Review geometry:** retain the Cp-TSR series but resolve its c/R before solidity/opacity calculations. Eight curves have this status.
- **Reference paper:** the original PDF supporting useful curves; keep it. No reference-only curve CSVs are included.

## Decisions and assumptions

1. User subsequently approved constant nominal-air viscosity estimates. See the final section for the applied nu=1.50e-5 m2/s assumption, affected rows, calculated values and limitations. Field-site data with unresolved geometry are not assigned fabricated constants.
2. Re_rot retains the reported rotational chord Reynolds number, defined as omega R c / nu. It is not diameter Reynolds number. Where this definition applies, Re_D = 2 Re_rot / [(c/R) TSR], evaluated point by point. No viscosity assumption is required for that conversion. Re_D remains blank in the constant metadata table.
3. Fixed-U Blackwell runs instead use Re_D = rho U (2R) / mu once fluid properties are justified. NASA Fig 8 pools speeds, so it cannot be assigned one curve-wide Re_D.
4. Blank pitch is not zero. Rotor tilt, virtual incidence and manufacturing twist are not substituted for a uniform physical alpha_p. No cross-paper pitch sign convention is imposed.
5. Source solidity is recorded in Notes, with its definition. Do not equate blade-area solidity with the notebook’s N(c/R)/(2*pi). Mixed chord and curved blades require explicit geometry conventions.
6. Preserve original measured/digitized negative Cp values. If using the previously requested nonnegative-performance subset, remove Cp < 0 only in a working copy and document affected points. No numerical points have been deleted in this package.
7. Cp/TSR point-level validation awaits extracted CSVs. Do not automatically discard Cp > 0.593 without checking area normalization, confinement and corrections.
8. The uploaded default metadata and rename maps are unchanged. These files apply only to the troposkein collection. Notebook ingestion was not edited or tested.

## Source audit and missing-figure check

### Battisti2016

Tables 1-4, PDF pp4-5; 4 curves. Figs 3-4 repeat torque-coefficient data; Figs 5-6 are thrust, not performance.

Cp = TSReq * CQ,aero. N=3, 200/300 rpm, upright/15-degree tilt. Geometry is not verified from this brief paper; do not borrow 2018 dimensions. Obtain the companion geometry report. All four tabulated performance conditions are represented.

| Curve_ID | Target and series |
|---|---|
| Battisti2016-C001 | Table 1: 200 rpm; tilt 0 deg |
| Battisti2016-C002 | Table 2: 300 rpm; tilt 0 deg |
| Battisti2016-C003 | Table 3: 200 rpm; tilt 15 deg |
| Battisti2016-C004 | Table 4: 300 rpm; tilt 15 deg |

### Battisti2018

Table 9 PDF p19; 1 troposkien curve corresponding to Fig 10. Exclude H-shaped data and wake/load figures.

Use actual per-row RPM, U, rho and Qaero: omega=2*pi*RPM/60; TSR=omega*0.755/U; Cp=Qaero*omega/(0.5*rho*1.5*U^3). N=3, c=0.085 m, R=0.755 m, c/R=0.112583. Tables 3 and 5 PDF pp4-5 supply geometry. No additional independent troposkien performance series selected.

| Curve_ID | Target and series |
|---|---|
| Battisti2018-C001 | Table 9: Troposkien; nominal 400 rpm |

### Blackwell1976

Figs 6-10 PDF pp34-38: 16 fixed-rotational-Re curves. Figs 15-19 PDF pp43-47: 10 fixed-U curves.

Table I PDF p25: measured R=0.9798 m, A=2.5944 m2; chords 0.08815/0.07346/0.05877 m. Use measured radius, not nominal 1 m. Fig 10 legend resolves conflicting table entries. Filled peak-torque markers belong to their parent curve. Figs 11-14 and 20 reorganize runs; Fig 21 adds reference data. Do not import these again.

| Curve_ID | Target and series |
|---|---|
| Blackwell1976-C001 | Fig 6: 180 rpm; Re_c 104000; circle |
| Blackwell1976-C002 | Fig 6: 267 rpm; Re_c 150000; square |
| Blackwell1976-C003 | Fig 6: 500 rpm; Re_c 290000; triangle |
| Blackwell1976-C004 | Fig 7: 216 rpm; Re_c 101000; circle |
| Blackwell1976-C005 | Fig 7: 320 rpm; Re_c 151000; square |
| Blackwell1976-C006 | Fig 7: 600 rpm; Re_c 278000; diamond |
| Blackwell1976-C007 | Fig 8: 270 rpm; Re_c 101000; circle |
| Blackwell1976-C008 | Fig 8: 400 rpm; Re_c 154000; square |
| Blackwell1976-C009 | Fig 8: 525 rpm; Re_c 200000; diamond |
| Blackwell1976-C010 | Fig 9: 180 rpm; Re_c 106000; circle |
| Blackwell1976-C011 | Fig 9: 267 rpm; Re_c 156000; square |
| Blackwell1976-C012 | Fig 9: 350 rpm; Re_c 204000; down triangle |
| Blackwell1976-C013 | Fig 9: 500 rpm; Re_c 290000; diamond |
| Blackwell1976-C014 | Fig 10: 267 rpm; Re_c 104000; circle |
| Blackwell1976-C015 | Fig 10: 400 rpm; Re_c 155000; square |
| Blackwell1976-C016 | Fig 10: 525 rpm; Re_c 200000; diamond |
| Blackwell1976-C017 | Fig 15: U 9 m/s; square |
| Blackwell1976-C018 | Fig 15: U 11 m/s; circle |
| Blackwell1976-C019 | Fig 16: U 9 m/s; square |
| Blackwell1976-C020 | Fig 16: U 11 m/s; circle |
| Blackwell1976-C021 | Fig 17: U 7 m/s; circle |
| Blackwell1976-C022 | Fig 17: U 9 m/s; square |
| Blackwell1976-C023 | Fig 18: U 9 m/s; square |
| Blackwell1976-C024 | Fig 18: U 11 m/s; circle |
| Blackwell1976-C025 | Fig 19: U 7 m/s; circle |
| Blackwell1976-C026 | Fig 19: U 9 m/s; square |

### Muraca1976

Fig 8 PDF p27: NASA open circles only, retained as one mixed-speed dataset.

Exclude filled NAE/NRC circles and analytical lines. Average chord 5.58 in = 0.141732 m; the printed 0.0142 m is a conversion inconsistency. R=2.1336 m; c/R=0.066429. Geometry PDF p7; speeds Table I PDF p18. Blade twist is not uniform pitch. No additional independent NASA Cp-TSR figure selected.

| Curve_ID | Target and series |
|---|---|
| Muraca1976-C001 | Fig 8: NASA experimental open circles; mixed test speeds |

### Sheldahl1977

Fig 9 PDF p25: four campaigns, including both 150a and 150b rpm.

PDF p13: curved NACA0012 portion c=0.19 m; streamlined end sections c=0.10 m. Source solidity 0.26 assumes 0.19 m throughout. Nominal D=5 m suggests midspan c/R=0.076, but this is not verified uniform-chord geometry; cToR is blank. Fig 7 repeats earlier runs; Figs 8/10 use another normalization; Figs 11-14 revisit data/model/anemometer comparisons. The two 150-rpm campaigns are distinct.

| Curve_ID | Target and series |
|---|---|
| Sheldahl1977-C001 | Fig 9: 125 rpm campaign; square |
| Sheldahl1977-C002 | Fig 9: 150b rpm campaign; triangle |
| Sheldahl1977-C003 | Fig 9: 150a rpm campaign; circle |
| Sheldahl1977-C004 | Fig 9: 162.5 rpm campaign; diamond |

### Sheldahl1980

Fig 7 PDF p22: three N=3 curves. Fig 9 PDF p28: two N=2 curves.

NACA0015 throughout; chord 0.1524 m (PDF p12); source c/R=0.067 (PDF p33). Retain the reported ratio rather than recomputing from nominal 5-m diameter; verify absolute radius before further geometry calculations. Site altitude 1658 m. Figs 8/10 are alternative normalization; Figs 11-13 repeat experimental comparisons or add model results; Fig 14 is drag. Repeated scan pages are not new datasets.

| Curve_ID | Target and series |
|---|---|
| Sheldahl1980-C001 | Fig 7: 125 rpm; circle |
| Sheldahl1980-C002 | Fig 7: 137.5 rpm; square |
| Sheldahl1980-C003 | Fig 7: 150 rpm; diamond |
| Sheldahl1980-C004 | Fig 9: 162.5 rpm; circle |
| Sheldahl1980-C005 | Fig 9: 175 rpm; square |

## Standing workflow

For each new paper, first identify experimental Cp-TSR curves and repeated baselines; then audit geometry and conditions, list missing figures and record decisions here. Ask unresolved assumptions one at a time in chat. Return only these two tables and this readable log unless another output is requested. Keep original PDFs and raw measurements intact.

The six supplied papers are covered here. The Sandia 17-m and 34-m reports were not among these six PDFs; this audit does not certify their figure completeness.

## Checks performed

41 unique curve IDs and filenames; 6 PDF references; exact template column order; source-wise consecutive IDs; matching names across both tables. All proposed filenames are shorter than 259 characters. Long parent folders can still exceed a Windows full-path limit.

## Metadata re-audit and source spacing — 24 October 2026

- Added exactly one fully empty separator row between each source in both CSVs (five separators). IDs and proposed filenames are unchanged. Separators are presentation only: ignore rows with no values when reading these tables programmatically.
- Rechecked all 41 populated metadata records: blade counts, available chord/radius ratios, freestream-speed labels, rotational Reynolds numbers, profile descriptions, curve identity, figure/page references, formulas and unknown-value handling. Compared source dimensions and legends, rather than assuming the previous map was correct.
- Battisti2018: filled previously blank Struts with “no”, supported by PDF p4 section 2.2.2. This describes blade-support spokes, not the absence of a shaft or hub. Added the paper’s correction treatment to Notes: no blockage correction; bearing losses corrected. The 174350 Reynolds value is the nominal zero-wind Table 6 reference.
- Numerical checks: Battisti2018 c/R = 0.085/0.755 = 0.112583; Blackwell ratios from measured R=0.9798 m are 0.089967, 0.074974 and 0.059982; Muraca ratio = 5.58/84 = 0.066429. Six-decimal rounding is consistent with filenames. Sheldahl1980 0.067 is source-reported, not recomputed from nominal diameter.
- Rechecked Blackwell’s 16 rotational-Re legend values and 10 fixed-U conditions; Sheldahl1977’s four campaigns; Sheldahl1980’s five rpm/Re cases; Battisti’s four 2016 conditions and one 2018 series. No numerical metadata changes resulted from this recheck.
- Known source issues remain documented: Blackwell Table I versus Fig 10 inconsistency; Muraca imperial-to-metric chord typo; Sheldahl1980 nominal diameter versus reported c/R discrepancy. These are not independently resolved experimental measurements.
- Eight c/R values remain unresolved. Blank pitch, density, viscosity and curve-wide Re_D values remain unknown/not applicable as constants; they have not been “verified as zero.” Remaining blank optional properties are not inferred from rotor type.
- Limits: this validates recorded metadata and its source basis. It cannot validate unprovided digitized Cp/TSR points, establish unresolved geometry, or certify every potential repeated curve by numerical point matching.

## Reynolds-number instructions by source

Use the source-specific procedure below. None of these metadata rows currently contains a directly supplied diameter Reynolds number: ten Blackwell entries are calculated estimates; the other rows require pointwise calculation or missing geometry. Re_rot is retained separately.

The Excel workbook has a Re_D Calculations tab with one row per curve, linked by Curve_ID. It records the applicable equation and missing inputs, including the ten already estimated fixed-U curves. It is a calculation guide, not a populated performance-point table. CSV files cannot contain tabs; their Notes columns carry the same source-specific instructions.

For direct speed calculations, the approved reference assumption is nu=1.50e-5 m2/s (kinematic viscosity), equivalent to mu=1.80e-5 Pa s and rho=1.20 kg/m3. These are assumed air properties, not measured conditions. Do not overwrite measured density used to calculate Cp.

### Battisti2016

Re_D = 2*Re_rot/(cToR*TSR)

Blocked: matching cToR must be verified first. Reported Re_rot=138000 or 205000 is rotational chord Reynolds, not Re_D. Tables 1-4, PDF pp4-5. Use each positive TSR and the matching geometry; do not borrow Battisti2018 geometry. No additional viscosity assumption is needed for a valid reported-Re conversion.

### Battisti2018

Re_D = 1.51*U_m_s/0.000015

Pointwise estimate; enter each Table 9 wind speed. D=1.51 m, assumed nu=1.50e-5 m2/s; Re_D=100666.666667*U_m_s. Table 9 is PDF p19, printed p443. Use matching table-row speed. The nominal zero-wind Re_rot=174350 must not be used as a constant diameter Reynolds number.

### Blackwell1976 - fixed-rpm curves (Figs 6-10)

Re_D = 2*Re_rot/(cToR*TSR)

Pointwise conversion; enter each positive TSR. Figs 6-10, PDF pp34-38. Use the curve-specific reported rotational chord Reynolds and cToR in metadata. Preserve the source velocity/correction convention. No additional viscosity assumption is needed. Do not evaluate at TSR=0.

### Blackwell1976 - fixed-U curves (Figs 15-19)

Re_D = 1.9596*U_m_s/0.000015

Constant estimate already entered in metadata. Figs 15-19, PDF pp43-47; R=0.9798 m, assumed nu=1.50e-5 m2/s. U=7,9,11 m/s gives Re_D=914480,1175760,1437040 respectively. RPM and TSR change, but Re_D stays constant at fixed U and viscosity. These are estimates, not source-reported diameter Reynolds numbers.

### Muraca1976

Re_D = 4.2672*U_m_s/0.000015

Pointwise estimate; enter each complete Table I wind speed. Table I, PDF p18 pairs U, Cp and TSR; prefer it over digitizing Fig 8. D=4.2672 m; assumed nu=1.50e-5 m2/s; Re_D=284480*U_m_s. Run 105 has missing performance entries. Fig 8 pools conditions, so no single curve-wide Re_D.

### Sheldahl1977

Re_D = 2*(2*pi*RPM/60)*2.5^2/(0.000015*TSR)

Pointwise nominal-geometry estimate; enter each positive TSR. Fig 9, PDF p25; RPM=125,150a,150b,162.5 by campaign. Assumes nominal D=5 m, R=2.5 m and nu=1.50e-5 m2/s. Field air properties are approximated. Keep the two 150-rpm campaigns separate. This route does not need chord; it does not resolve cToR or solidity.

### Sheldahl1980

Re_D = 2*Re_rot/(0.067*TSR)

Pointwise conversion; enter each positive TSR. Figs 7 and 9, PDF pp22/28; use each curve's reported Re_rot and source cToR=0.067 (PDF p33). No additional viscosity assumption is needed. Retain the reported-ratio versus nominal-diameter discrepancy. Do not evaluate at TSR=0.

### Calculation boundaries

The rotational conversion is valid only for Re_rot=omega*R*c/nu and TSR=omega*R/U with matching conventions. A freestream chord Reynolds number instead gives Re_D=2*Re_c/cToR, without a TSR divisor. Blank Re_D means unavailable as a curve-wide constant, not zero. Store varying Re_D on each extracted performance row; do not copy one point into every row.

### Changes in this revision

Replaced the overlapping general Reynolds discussions with one explicit procedure per source and a separate fixed-U Blackwell procedure. Added instructions to metadata Notes and source Audit_notes, plus the Excel Re_D Calculations tab. Preserved all curve IDs, filenames, separators and existing numerical metadata. Rename map unchanged.
