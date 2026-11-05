# QR Code Generator

A beginner-friendly Flask web application that turns a website link into a
downloadable PNG QR code.

The application accepts HTTP and HTTPS links, generates the QR code in memory,
and displays it on the same page. It does not need to save QR images to the
server.

## Features

- Accepts `http://` and `https://` links
- Validates the submitted URL in Python
- Generates QR codes with the Python `qrcode` package
- Displays the QR code in the browser
- Allows the user to download the QR code as `qr-code.png`
- Keeps the submitted link in the form after generation
- Shows validation errors for invalid links
- Uses responsive CSS for smaller screens
- Generates images in memory rather than storing them on disk

## How it works

1. The visitor enters a URL in the HTML form.
2. The browser sends the form to Flask with a `POST` request.
3. Flask reads the URL from `request.form`.
4. Python checks that the URL uses HTTP or HTTPS.
5. The `qrcode` package creates a QR image.
6. Pillow saves the image into an in-memory buffer.
7. Flask encodes the image and sends it back to the HTML template.
8. The browser displays the QR code and provides a download link.

The generated QR image is derived from the submitted URL. The current version
does not have accounts, a database, analytics, or server-side QR-code history.

## Project structure

```text
qrcode_generator/
├── app.py                 # Flask routes and QR-code generation
├── requirements.txt       # Python dependencies
├── render.yaml            # Render deployment configuration
├── templates/
│   └── index.html         # Main page and Jinja template
├── static/
│   └── styles.css         # Page styling
└── .gitignore             # Files that should not be committed
```

## Run locally

Open PowerShell in the project folder and create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

Start Flask:

```powershell
python app.py
```

Open <http://127.0.0.1:5000> in your browser.

The local Flask server uses debug mode to make development easier. Do not use
the debug server as the production server.

## Deploy to Render

1. Push the repository to GitHub.
2. In Render, choose **New → Blueprint** or **New → Web Service**.
3. Connect the GitHub repository.
4. If using a Blueprint, Render can read the included `render.yaml`.
5. If configuring the service manually, use:

```text
Build command: pip install -r requirements.txt
Start command: gunicorn --bind 0.0.0.0:$PORT app:app
Health check path: /
```

Render runs the application with Gunicorn, a production WSGI server.

## Privacy and security

This project is designed to avoid unnecessary storage:

- QR images are generated in memory.
- The application has no account system or database yet.
- No analytics or tracking code is included.
- URL validation happens on the server, not only in the browser.
- The `.gitignore` prevents the local virtual environment and common secret
  files from being committed.

These measures reduce risk but cannot guarantee that a public website will
never be attacked or breached. Before adding accounts or history, the project
will need secure password hashing, session protection, CSRF protection, rate
limiting, account deletion, data-retention rules, and a privacy notice.

Never commit passwords, API keys, database credentials, or other secrets.
