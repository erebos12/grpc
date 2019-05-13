import grpc

from flask import Flask, jsonify
import service_pb2
import service_pb2_grpc

app = Flask(__name__)

channel = grpc.insecure_channel('localhost:4040')
stub = service_pb2_grpc.AddServiceStub(channel)


@app.route("/", methods=['GET'])
def say_hello():
    return jsonify({"message": "I'm alive!"})


@app.route('/python/mult/<a>/<b>', methods=['GET'])
def multiply(a, b):
    app.logger.info(f"python-grpc-client: multiply request received: {a}, {b}")
    try:
        response = stub.Multiply(service_pb2.Request(a=int(a), b=int(b)))
        return jsonify({"result": response.result})
    except Exception as e:
        error = str(e)
        return jsonify({"Error": "{}".format(error)})


@app.route('/python/add/<a>/<b>', methods=['GET'])
def add(a, b):
    app.logger.info(f"python-grpc-client: add request received: {a}, {b}")
    try:
        response = stub.Add(service_pb2.Request(a=int(a), b=int(b)))
        return jsonify({"result": response.result})
    except Exception as e:
        error = str(e)
        return jsonify({"Error": "{}".format(error)})
