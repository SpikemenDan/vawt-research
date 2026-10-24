# Troposkein: short filenames, metadata, and decisions

## Use these two tables

- metadata_troposkein.csv: one row per retained experimental curve, using exactly the default metadata columns and their order.
- rename_map_troposkein.csv: the default five columns; includes six supplied PDFs and 41 planned curve CSVs. No screenshots or extracted performance CSVs were supplied for this six-paper set. “Not created yet” is literal; these rows are extraction targets.

Filename: `SourceYear (Fig 4) (N = 3) (cToR = 0.085714) (C001).csv`. Numerical-table sources use `Table` instead of `Fig`.

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

## Reynolds-number interpretation for the postdoc

A blank Re_D in the curve metadata does not mean zero Reynolds number, and it does not necessarily mean that Reynolds number cannot be calculated. This metadata table has one row per curve. Many of these experiments vary wind speed while holding rpm approximately constant, so their diameter-based Reynolds number varies along that single Cp-TSR curve. A single metadata value would conceal that variation.

### Definitions and conversion

Diameter Reynolds number: Re_D = U(2R)/nu = rho U(2R)/mu. Here U is freestream speed, R is maximum rotor radius, nu is kinematic viscosity, mu is dynamic viscosity, and nu = mu/rho. Density is needed when using dynamic viscosity.

For the particular rotational chord definition Re_rot = omega R c/nu, together with TSR = omega R/U, algebra gives:

Re_D(TSR) = 2 Re_rot / [(c/R) TSR].

This conversion requires matching radius, chord, viscosity and velocity conventions. It applies at positive TSR; it must not be evaluated at TSR=0. It is not valid merely because another paper calls its quantity “rotational Reynolds number”: that paper’s actual equation must first be checked. If a nominal Re_rot is substituted, the result inherits that approximation. Wind-tunnel correction conventions must also be kept consistent.

No additional viscosity assumption is needed when converting an applicable, known Re_rot using this identity. A freestream chord Reynolds number Re_c = U c/nu has a different conversion: Re_D = 2 Re_c/(c/R), with no TSR divisor.

### What applies to each supplied source

| Source / cases | Treatment of Re_D |
|---|---|
| Battisti2016, Tables 1-4 | Fixed nominal rpm with varying wind speed. Convert point by point from reported rotational chord Re once c/R is verified. Geometry is presently unresolved; retain the reported Re_rot in the meantime. |
| Battisti2018, Table 9 | Wind speed varies. Calculate Re_D for each table row using R=0.755 m, its U and density, and viscosity estimated from its temperature with a documented property model. Table 6’s 174350 is a nominal zero-wind rotational reference, not a measured constant Re_D for the performance curve. |
| Blackwell1976, Figs 6-10 | Fixed rotational chord Reynolds-number runs with changing freestream speed. Use Re_D(TSR)=2 Re_rot/[(c/R) TSR] point by point, retaining the source’s correction conventions. |
| Blackwell1976, Figs 15-19 | Fixed wind-speed runs with changing rpm. Re_D may be represented by a constant per curve if fluid properties are treated as constant. An estimate can be made from the reported speed and R=0.9798 m using explicitly stated air properties. These estimates are now entered in metadata; see the final section. |
| Muraca1976, Fig 8 | Open-circle data pool test speeds. Do not assign one constant Re_D or infer separate speeds from identical markers. Reconstruct point conditions from Table I if a reliable measurement-to-point mapping can be established. |
| Sheldahl1977, Fig 9 | Fixed-rpm campaigns with varying wind speed. Conversion is pointwise and requires a verified equatorial c/R consistent with the source Re definition. Mixed blade chords must not be collapsed into an undocumented uniform geometry. |
| Sheldahl1980, Figs 7 and 9 | Fixed-rpm campaigns with varying wind speed. Convert point by point from reported rotational chord Re and reported c/R=0.067. The result inherits the reported ratio’s rounding and the geometry discrepancy already flagged. |

### Is this true for all sources?

No. Re_D and TSR need not both vary. At fixed U, radius and viscosity, changing rpm changes TSR but leaves Re_D constant. At fixed rpm and fluid properties, changing U changes both; their product is constant for fixed geometry. If rpm and fluid properties also change, neither simplification is guaranteed.

The source-by-source conclusions above apply to these six uploaded troposkein papers. They should not be imposed on the separate default collection without checking each experiment’s protocol and Reynolds-number definition. In particular, neither “all Re_D values must be blank” nor “all curves can use one constant Re_D” is a general rule.

### How the data should be stored

For constant-condition cases, put the reported or explicitly estimated Re_D in curve metadata and repeat it down the performance CSV if required. For varying-condition cases, compute Re_D in each performance CSV row and leave the curve-level constant blank, with its basis explained. A value evaluated at peak Cp may be saved as a separately identified peak-condition summary; it must not be presented as constant across the full curve.

Before the nominal-air update, blank Re_D fields included pointwise values still to be calculated, fixed-U estimates not yet assigned, and unresolved geometry or mixed-point provenance. The fixed-U estimates are now filled below. This explains the earlier blank fields; the subsequent user-approved estimates are documented in the final section below.

## User-approved nominal-air Reynolds estimates — 24 October 2026

This section supersedes earlier statements that no viscosity estimate was applied. All six supplied experiments use air. The adopted reference is nu=1.50e-5 m2/s, equivalent to assumed mu=1.80e-5 Pa s and rho=1.20 kg/m3. These are nominal properties, not measured conditions. Re_basis identifies estimated values. Do not use the assumed density to overwrite measured density in Cp calculations.

Ten fixed-U Blackwell curves now have a constant estimated Re_D. Radius is measured R=0.9798 m, so Re_D=U*1.9596/1.50e-5. Numerical labels do not imply integer-level physical precision.

| Curve_ID | U (m/s); estimated Re_D |
|---|---|
| Blackwell1976-C017 | 9; 1175760 |
| Blackwell1976-C018 | 11; 1437040 |
| Blackwell1976-C019 | 9; 1175760 |
| Blackwell1976-C020 | 11; 1437040 |
| Blackwell1976-C021 | 7; 914480 |
| Blackwell1976-C022 | 9; 1175760 |
| Blackwell1976-C023 | 9; 1175760 |
| Blackwell1976-C024 | 11; 1437040 |
| Blackwell1976-C025 | 7; 914480 |
| Blackwell1976-C026 | 9; 1175760 |

For the remaining calculable cases, the following expressions produce a Re_D for each performance-data row. They are documented in metadata Notes; they must not be pasted into the numerical Re_D constant column. Performance CSV coordinates are not present for these curves, so no per-TSR values have been fabricated.

| Curve_ID | Pointwise Re_D expression and basis |
|---|---|
| Battisti2018-C001 | 100666.666667*U_m_s; nominal-air estimate; Table 9 |
| Blackwell1976-C001 | 2412763.365/TSR; nominal-air estimate |
| Blackwell1976-C002 | 3578932.324/TSR; nominal-air estimate |
| Blackwell1976-C003 | 6702120.457/TSR; nominal-air estimate |
| Blackwell1976-C004 | 2895316.038/TSR; nominal-air estimate |
| Blackwell1976-C005 | 4289357.093/TSR; nominal-air estimate |
| Blackwell1976-C006 | 8042544.549/TSR; nominal-air estimate |
| Blackwell1976-C007 | 3619145.047/TSR; nominal-air estimate |
| Blackwell1976-C008 | 5361696.366/TSR; nominal-air estimate |
| Blackwell1976-C009 | 7037226.480/TSR; nominal-air estimate |
| Blackwell1976-C010 | 2412763.365/TSR; nominal-air estimate |
| Blackwell1976-C011 | 3578932.324/TSR; nominal-air estimate |
| Blackwell1976-C012 | 4691484.320/TSR; nominal-air estimate |
| Blackwell1976-C013 | 6702120.457/TSR; nominal-air estimate |
| Blackwell1976-C014 | 3578932.324/TSR; nominal-air estimate |
| Blackwell1976-C015 | 5361696.366/TSR; nominal-air estimate |
| Blackwell1976-C016 | 7037226.480/TSR; nominal-air estimate |
| Muraca1976-C001 | 284480*U_m_s; nominal-air estimate; requires point provenance |
| Sheldahl1980-C001 | 7462686.567/TSR; reported-Re_rot conversion; source rounded geometry |
| Sheldahl1980-C002 | 8358208.955/TSR; reported-Re_rot conversion; source rounded geometry |
| Sheldahl1980-C003 | 8955223.881/TSR; reported-Re_rot conversion; source rounded geometry |
| Sheldahl1980-C004 | 9850746.269/TSR; reported-Re_rot conversion; source rounded geometry |
| Sheldahl1980-C005 | 10626865.672/TSR; reported-Re_rot conversion; source rounded geometry |

Battisti2018: use measured U from each Table 9 row. Its speed range gives approximately 3.171e5 to 2.01434e6 for this assumed nu. For Blackwell fixed-rpm curves, the new nominal-air expression and the existing reported-Re_rot conversion are alternative estimates; they can differ because the source Re and assumed properties need not coincide. Preserve reported Re_rot and consistently identify which method is used.

Muraca: the numerical U-to-Re factor is established, but a reliable wind-speed assignment to each plotted point is still needed. Battisti2016 and Sheldahl1977 still require verified geometry. Assumed viscosity alone cannot recover unknown radius or chord ratio. Sheldahl1980 uses the reported-Re_rot conversion without imposing sea-level viscosity on the 1658-m field site; the source geometry discrepancy remains flagged.

Validation: 10 populated constant Re_D values; 41 curve IDs retained; five source separator rows retained; filenames and rename map unchanged. Estimates checked using both U D/nu and rho U D/mu. No performance measurements were altered.
