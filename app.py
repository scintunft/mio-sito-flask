import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def home():
    return render_template("index.html")

# Servire file statici manualmente (opzionale, Flask lo fa già di default)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Usa la porta fornita da Render o 5000 in locale
    app.run(host='0.0.0.0', port=port, debug=True)
