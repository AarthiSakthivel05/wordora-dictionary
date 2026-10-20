# LexiLoom Dictionary App

Professional-looking dictionary project with HTML, CSS, JavaScript, Python Flask and a free public dictionary API.

## Features
- API-based English word search, definitions, examples and phonetics
- Listen button with API audio and browser speech fallback
- Voice search in supported Chrome/Edge browsers (microphone permission needed)
- Favourite collection and search history stored in browser local storage
- Related word buttons, copy details, word of the day and responsive multi-screen navigation

## Run in VS Code (Windows)
1. Extract this ZIP and open the `LexiLoom_Dictionary` folder in VS Code.
2. Open Terminal > New Terminal.
3. Run `py -m venv .venv` (optional).
4. If you created the environment, activate it: ` .\.venv\Scripts\Activate.ps1 `
5. Install dependencies: `py -m pip install -r requirements.txt`
6. Start the app: `py app.py`
7. Open `http://127.0.0.1:5000` in Chrome.

Keep the terminal open while using the app. Press Ctrl+C to stop the server.
For Render hosting, use start command `gunicorn app:app`.
