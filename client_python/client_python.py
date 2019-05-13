import grpc

from flask import Flask, jsonify, request
import service_pb2
import service_pb2_grpc
import logging

app = Flask(__name__)


@app.route("/", methods=['GET'])
def say_hello():
    return jsonify({"message": "I'm alive!"})


@app.route('/multiply/<a>/<b>', methods=['GET'])
def multiply(a, b):
    app.logger.info(f"python-grpc-client: multiply request received: {a}, {b}")
    try:
        with grpc.insecure_channel('localhost:4040') as channel:
            stub = service_pb2_grpc.AddServiceStub(channel)
            response = stub.Multiply(service_pb2.Request(a=int(a), b=int(b)))
        return jsonify({"result": response.result})
    except Exception as e:
        error = str(e)
        return jsonify({"Error": "{}".format(error)})
