# AIRA 2.0 — Automated Airfare Intelligence & Real-time Analytics

## Professional SIH26056 Prototype

AIRA 2.0 is rebuilt around the complete requirements supplied for SIH26056.

### Included
- 24 representative routes covering major and selected regional airports
- Five understandable booking periods: Tomorrow, 1 Week Before, 15 Days Before, 1 Month Before, 45 Days Before
- Multi-source airline/OTA connector architecture
- Playwright-ready, compliance-first collection layer and daily scheduler architecture
- Standard fare schema and data cleaning
- Duplicate removal, missing values, sold-out/cancelled handling
- Base fare, taxes, UDF, convenience charge and total fare
- Route + booking-period IQR outlier detection
- Daily, weekly and monthly Airfare Price Index (APIx)
- Heatmap and booking-time price analytics
- AIRA Fare Movement Explanation Engine
- AIRA TrustChain (SHA-256 tamper-evident records)
- 30-day back-testing workflow and validation metrics
- Versioned REST API, automated tests and professional React UI

### Important prototype note
The bundled data is synthetic so every feature can run immediately. It must not be presented as live-scraped airline data. Replace sample observations and demo reference data with permitted real observations and public/official reference data before final field validation. Live source adapters must use permitted access methods. This project does not bypass CAPTCHAs, anti-bot controls or access restrictions.

## Run
```bash
python -m venv .venv
```
Windows PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```
Install and start backend:
```bash
pip install -r requirements.txt
python -m backend.app
```
Open a second terminal:
```bash
cd frontend
npm install
npm run dev
```
