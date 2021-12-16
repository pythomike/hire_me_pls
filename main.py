from flask import Flask, Response, jsonify, json
from datetime import datetime, timedelta


app = Flask(__name__)
start = datetime.now()
ready_threshhold = int(10)

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.route('/')
def index():
    return "Hello world"

@app.route('/status/alive')
def pulse_check():
    return Response(status=200)

@app.route('/status/ready')
def ready_check():
    lifetime = (datetime.now() - start).total_seconds()
    
    if lifetime < ready_threshhold:
        return Response(json.dumps({'ready': False}), status=500)
    else:
        return Response(json.dumps({'ready': True}), status=200)


if __name__ == "__main__":
    app.run(debug=True)