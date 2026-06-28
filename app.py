from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>🚀 Chan's DevOps Dashboard</h1>
    <p><strong>Status:</strong> Running ✅</p>
    <p><strong>Hostname:</strong> {socket.gethostname()}</p>
    <p><strong>Time:</strong> {datetime.now()}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)