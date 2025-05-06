# Importing Libraries
from flask import Flask, request
import json
import datetime
import os

app = Flask(__name__)

# Double Checking if the log files and directory exists, if not creates said directory and files
LOG_FILE = "logs/honeypot_logs.jsonl"
os.makedirs("logs", exist_ok=True)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def log_request(path):
    log_entry = {
        "timestamp": str(datetime.datetime.now()),
        "remote_ip": request.remote_addr,
        "method": request.method,
        "path": path,
        "headers": dict(request.headers),
        "args": request.args.to_dict(),
        "body": request.get_data(as_text=True),
        "user_agent": request.user_agent.string
    }

    # Open log file, append JSON objects to file (1 at a time)
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    # Simulating service unavailable
    return "Service Unavailable", 503

@app.route('/admin', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def fake_login():
    log_entry = {
        "timestamp": str(datetime.datetime.utcnow()),
        "remote_ip": request.remote_addr,
        "method": request.method,
        "path": request.path,
        "headers": dict(request.headers),
        "args": request.args.to_dict(),
        "body": request.get_data(as_text=True),
        "user_agent": request.user_agent.string,
        "honeypot_section": "login"
    }

    # Save login attempt
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    # Respond like a real login page, implementing HTML Code
    if request.method == "POST":
        return "Invalid username or password.", 401
    else:
        return '''
        <html>
        <head><title>Login</title></head>
        <body>
        <h2>Please Login</h2>
        <form method="POST">
            Username: <input type="text" name="username"/><br/>
            Password: <input type="password" name="password"/><br/>
            <input type="submit" value="Login"/>
        </form>
        </body>
        </html>
        '''

# Hard coded port, in future will ask user to input port number of their choice. 
if __name__ == '__main__':
    print("Honeypot running on http://0.0.0.0:8080")
    app.run(host="0.0.0.0", port=8080, debug=False)
