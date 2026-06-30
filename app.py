from flask import Flask, render_template
import socket
import platform
from datetime import datetime
import psutil
app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    current_time = datetime.now().strftime("%B %d, %Y %I:%M:%S %p")
    operating_system = platform.system()
    python_version = platform.python_version()
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent

    return render_template(
    "index.html",
    hostname=hostname,
    current_time=current_time,
    operating_system=operating_system,
    python_version=python_version,
    cpu_usage=cpu_usage,
    memory_usage=memory_usage,
    disk_usage=disk_usage
)

if __name__ == "__main__":
    app.run(debug=True)