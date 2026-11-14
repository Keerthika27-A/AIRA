# Requirement Mapping

| Requirement | Implementation |
|---|---|
| Multi-source architecture | Extensible airline/OTA adapter architecture |
| Ethical automation | No CAPTCHA or anti-bot bypass; rate-limiting architecture |
| 24 routes | Major and selected regional routes |
| Multiple booking windows | Tomorrow, 1 Week, 15 Days, 1 Month, 45 Days |
| Standard database fields | Origin, destination, carrier, source, fare components and availability |
| Cleaning | De-duplication, missing-data and availability handling |
| Outliers | IQR by route + booking period |
| Daily/weekly/monthly index | Separate versioned API endpoints |
| Heatmap | Dashboard heatmap view |
| Lead-time curve | Booking Guide page |
| API | `/api/v1/...` endpoints |
| Testing | Pytest tests |
| 30-day back-test | 30-day workflow with metrics |
| Professional UX | Plain-language public dashboard + analyst centre |

## Required final data replacements
The bundled demo dataset and reference comparison are intentionally labelled as synthetic/demo. Replace them with permitted real observations and publicly available official reference data before final external validation.
