# Joke of the Day (Flask)

A tiny Flask app that serves a fresh programmer joke on demand using `pyjokes`.

## Features
- One-click joke button
- Playful UI theme
- JSON endpoint at `/get_joke`

## Quickstart (Windows Bash)

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/Scripts/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app.py
```

4. Open your browser at:

- http://127.0.0.1:5000/

## API
- `GET /get_joke` → `{ "joke": "..." }`

## Notes
- If you change ports or host, update the fetch URL if needed.
- Jokes come from the `pyjokes` library.
