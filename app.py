import os
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")  # Specifica la cartella dei template

@app.route("/")
def home():
    return render_template("index.html")  

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  
    app.run(host="0.0.0.0", port=port)
