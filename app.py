import base64
from io import BytesIO
from urllib.parse import urlparse

import qrcode
from flask import Flask, render_template, request

app = Flask(__name__)


def is_valid_url(value):
    parsed_url = urlparse(value)

    return parsed_url.scheme in {"http", "https"} and bool(parsed_url.netloc)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    website_url = request.form.get("website-url", "").strip()

    if not is_valid_url(website_url):
        return render_template(
            "index.html",
            error="Please enter a valid HTTP or HTTPS URL.",
            website_url=website_url,
        ), 400

    qr_image = qrcode.make(website_url)

    image_data = BytesIO()
    qr_image.save(image_data, format="PNG")

    encoded_image = base64.b64encode(image_data.getvalue()).decode("utf-8")

    return render_template("index.html", qr_code=encoded_image, website_url=website_url)


if __name__ == "__main__":
    app.run(debug=True)
