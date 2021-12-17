from datetime import datetime
from flask import Flask, Response, jsonify, json


APP = Flask(__name__)
START = datetime.now()
READY_THRESHHOLD = int(10)

@APP.errorhandler(404)
def resource_not_found(e):
    return jsonify(error="Sorry, I can't find that"), 404

@APP.route('/')
def index():
    return "Hello world"

@APP.route('/status/alive')
def pulse_check():
    return Response(status=200)

@APP.route('/status/ready')
def ready_check():
    lifetime = (datetime.now() - START).total_seconds()
    if lifetime < READY_THRESHHOLD:
        return Response(json.dumps({'ready': False}), status=500)
    return Response(json.dumps({'ready': True}), status=200)


if __name__ == "__main__":
    APP.run()
