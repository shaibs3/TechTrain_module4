import os
import sys
from flask import Flask

app = Flask(__name__)

# Get the port from an environment variable
port = os.getenv('APP_PORT')

if not port or not port.isdigit() or not (3000 <= int(port) <= 5000):
    print("Error: APP_PORT must be a number between 3000 and 5000.")
    sys.exit(1)

@app.route("/")
def home():
    return "App is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(port))
