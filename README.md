# Bless Mawumenyo Zaglago | Portfolio

A static portfolio built with HTML, CSS and JavaScript. Hosted on Vercel at
https://bless-zaglago.vercel.app/ (the existing porfolio-rosy-zeta alias also works).

The October 2026 refresh includes five public projects, six credentials, Level 300
education details, expected graduation in 2028, contact links and a two-page CV.
Project filters and the theme toggle enhance a page that remains readable without
JavaScript. Browser storage is optional; reduced-motion preferences are respected.

## Preview

Run `python -m http.server 8080` from the repository root and open localhost:8080.
No framework build, API key, analytics service or package installation is required.

## Content and assets

- Portrait, neural-network loss plot and grade coefficients: supplied by the owner.
- `assets/fraud-roc.png`: actual output from the owner's fraud-detection repository.
- `assets/zagjobsearch.jpg`: public homepage screenshot captured 25 October 2026.
  Photography within that screenshot belongs to the live project's credited sources.
- Other SVG assets: original portfolio illustrations. SmartEvents is explicitly
  labelled as a system-design illustration, rather than a live interface screenshot.
- Credential issuer names identify learning providers. No fabricated certificate,
  verification badge, endorsement or credential URL is used.

ZagJobSearch and jobs.ac.ghana are presented as one evolving project. The fraud
prediction API runs locally. The grade-predictor dataset is generated; fitted
coefficients do not establish causal importance. Neural-network accuracy describes
its Iris test split. Metrics are owner/repository-reported results, not a new
independent model evaluation.

## CV

`scripts/build_resume.py` rebuilds `resume.pdf` using ReportLab and DejaVu Sans.
Its default font path targets Linux; adjust `FONT` for another local environment.
The generated PDF is committed, so deployment does not need Python dependencies.
The CV and site use the owner's supplied Level 300 / 2028 education update.
