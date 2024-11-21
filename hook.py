from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Verify that the request is from GitHub
    if request.method == 'POST':
        data = request.json
        if 'push' in data:  # Ensure it's a push event
            # Run your pull command here
            try:
                # Pull the latest changes from the repository
                subprocess.run(['git', '-C', r'C:\inetpub\webhook\ptmkb\webhook_listener\Tempo', 'pull'], check=True)
                return 'Success', 200
            except subprocess.CalledProcessError as e:
                return f'Error: {str(e)}', 500
        return 'No push event detected', 200
