from flask import Flask, request, send_from_directory
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

@app.route("/search", methods=['GET'])
def search():
    query = request.args.get("query")
    res = requests.get(f"https://api.tenor.com/v1/search?q={query}&key=YOUR_TENOR_API_KEY&limit=4")
    return json.dumps(res.json()), 200

@app.route('/ai-plugin.json', methods=['GET'])
def serve_plugin_manifest():
    return send_from_directory(directory='.well-known', filename='ai-plugin.json')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
