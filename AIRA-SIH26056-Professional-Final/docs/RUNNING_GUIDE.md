# Step-by-Step Run Guide
1. Extract the ZIP.
2. Open the main folder in VS Code.
3. Open terminal with Ctrl + backtick.
4. Run `python -m venv .venv`.
5. Activate: `.venv\Scripts\Activate.ps1` (PowerShell) or `.venv\Scripts\activate` (CMD).
6. Run `pip install -r requirements.txt`.
7. Start backend: `python -m backend.app`.
8. Keep backend running and open a second terminal.
9. Run `cd frontend`, `npm install`, then `npm run dev`.
10. Open the Vite URL shown in the terminal, usually `http://localhost:5173`.
11. Run tests anytime with `pytest backend/tests -q`.
