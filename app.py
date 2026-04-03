from bot import main as run_bot
from flask import Flask
import threading
import logging

app = Flask(__name__)

@app.route('/')
def health_check():
    return "bot running 24/7", 200

def start_flask():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.start()

    run_bot()
