# QR Code Generator

A Flask application that creates QR code PNGs from HTTP(S) links.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:5000>.

## Deploy to Render

Push this repository to GitHub, then create a Render Web Service from it. The included `render.yaml` supplies:

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn --bind 0.0.0.0:$PORT app:app`
- Health check: `/`

Render can also use these values when configuring the service manually.

Never commit `.venv`, passwords, API keys, or other secrets. The Flask development server is for local use only; Render runs Gunicorn.
