import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Renderizza il file index.html

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Usa la porta fornita da Render
    app.run(host="0.0.0.0", port=port)
