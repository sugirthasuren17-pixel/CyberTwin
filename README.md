<<<<<<< HEAD
# CyberTwin — Interactive Cyberattack Simulator
**Team:** OBSIDIAN NEXORA · **Event:** Cryptathon ’26  
**Tagline:** Detect the Threat. Preserve the Evidence. Take Back Control.

CyberTwin is a defensive, educational cyber-safety web app. It provides three branching learning simulations, explainable rule-based message triage, a local Evidence Vault, a report draft builder, learning modules, and a dashboard based on saved browser state.

## Run the app
### Option A — easiest (frontend only)
1. Install Node.js 20+.
2. Open a terminal in `frontend`.
3. Run `npm install`
4. Run `npm run dev`
5. Open the local URL printed by Vite (usually `http://localhost:5173`).

The frontend works without an AI service or backend. Incidents, learning progress, simulation progress, and reports are saved in this browser's `localStorage`.

### Option B — run the API too
In a second terminal:
1. Open `backend`.
2. Create a virtual environment (optional but recommended).
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `uvicorn app.main:app --reload --port 8000`
5. API health: `http://localhost:8000/api/health`; interactive API docs: `http://localhost:8000/docs`.

The UI uses a transparent local rule-based analysis engine by default. The FastAPI endpoint is available for testing/integration; no external AI service is used.

## Storage and privacy
Browser records are stored in the current browser's localStorage. They are not automatically backed up to a server and this app does not claim that localStorage is encrypted. Avoid storing passwords, OTPs, recovery codes, payment information, or unrelated sensitive personal data. Submitted URLs are treated as text only and are never opened or fetched by the analyzer.

## Safety disclaimer
"CyberTwin is an educational safety assistant. Its analysis is preliminary and may be incorrect. Verify through trusted official channels. This tool does not replace professional, legal, emergency, or official reporting services."

For immediate danger, contact a trusted person, campus authority, or appropriate local emergency service. Preparing a report here does not submit it to a platform or authority.

## Checks
Backend tests: `cd backend && pytest`
Frontend production build: `cd frontend && npm run build`
=======
# CyberTwin
Explainable cybersecurity analysis platform
>>>>>>> a68eb75b3ab1679484b713a34306b235369c08b2
