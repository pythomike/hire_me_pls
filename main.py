from flask import Flask, Response
from datetime import datetime, timedelta


app = Flask(__name__)
start = datetime.now()

@app.route('/')
def index():
    return "Hello world"

@app.route('/status/alive')
def pulse_check():
    return Response(status=200)

@app.route('/status/ready')
def ready_check():
    lifetime = (datetime.now() - start).total_seconds()
    if lifetime < 10:
        return Response("yea boye")
    return "Ready test"


if __name__ == "__main__":
    app.run(debug=True)