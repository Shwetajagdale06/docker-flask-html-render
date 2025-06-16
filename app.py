from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    msg = os.getenv("MSG", "Default message from Flask")
    return render_template("index.html", message=msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
