import os
from flask import Flask

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "dev")
TITLE_COLOR = "red"


@app.route("/")
def index():
    return f"""<!doctype html>
<html>
  <head><title>Preview Demo</title></head>
  <body style="font-family: sans-serif; text-align: center; margin-top: 15vh;">
    <h1 style="color: {TITLE_COLOR};">Preview Demo</h1>
    <p>Version : <strong>{VERSION}</strong></p>
  </body>
</html>"""


@app.route("/healthz")
def healthz():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
