
# Indonesian Seismicity Dashboard

An interactive web dashboard for mapping seismic zones in Indonesia (clustering) and estimating earthquake rates across regions (forecasting), with explicit statistical reasoning.

> Disclaimer: This is an educational analysis tool, not an early warning system.

## Research Questions

1. Where are the active seismic zones in Indonesia, and what are the characteristics of each zone (rate, depth, b-value)?
2. How many earthquakes with M >= 4.5 occur per 1-degree grid cell per month, and how well does the model perform compared to the historical rate baseline?
3. How large is the uncertainty in the estimated parameters (b-value, earthquake rate, and predictions)?

## Scope

- **Geographic Region:** Latitude -11 to 6, Longitude 95 to 141
- **Data Source:** USGS ComCat earthquake catalog, from 1990 to present, with M >= 4.0
- **Target:** Number of earthquakes with M >= 4.5 per 1-degree grid cell per month
- **Temporal Split:**
  - Training: <= 2018
  - Validation: 2019-2021
  - Testing: >= 2022

## Success Metrics (Defined Before Modeling)

- The best-performing model must outperform the historical rate baseline on the test dataset, measured using Poisson deviance and log-likelihood.
- Pass basic calibration tests (N-test and L-test, following the CSEP methodology) and include calibration plots.
- Key estimates must be reported with uncertainty intervals.
- If the model only marginally outperforms the baseline, the results will be reported transparently.

## Project Phases

- [x] Phase 0: Setup
- [ ] Phase 1: Data Acquisition
- [ ] Phase 2: Data Cleaning and Validation
- [ ] Phase 3: Catalog Statistics
- [ ] Phase 4: Seismic Zone Clustering
- [ ] Phase 5: Earthquake Forecasting
- [ ] Phase 6: Dashboard Development
- [ ] Phase 7: Testing and Documentation
- [ ] Phase 8: Deployment
