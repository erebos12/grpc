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
    logging.error("python grpc client multiply received {} and {}".format(a, b))
    try:
        with grpc.insecure_channel('localhost:4040') as channel:
            stub = service_pb2_grpc.AddServiceStub(channel)
            print("Sending request now...")
            response = stub.Multiply(service_pb2.Request(a=int(a), b=int(b)))
            print("Response is: {}".format(response.result))
        return jsonify({"result": response.result})
    except Exception as e:
        error = str(e)
        return jsonify({f"Error": "{}".format(error)})
