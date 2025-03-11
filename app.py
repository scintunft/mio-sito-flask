import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Sito Flask online!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Usa la porta di Render, altrimenti 5000
    app.run(host="0.0.0.0", port=port)