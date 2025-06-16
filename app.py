from flask import Flask, render_template
import os

app = Flask(__name__)
msg = os.getenv("MSG", "Hello from Flask in Docker!")

@app.route('/')
def home():
    return render_template("index.html",message=msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

