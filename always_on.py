from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def serve_log_file():
    return send_from_directory('.', 'roulette_log.txt')

if __name__ == "__main__":
    app.run(port=8000)
