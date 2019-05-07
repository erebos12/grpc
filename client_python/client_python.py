import logging

import grpc

import service_pb2_grpc
import service_pb2


def run():
    with grpc.insecure_channel('localhost:4040') as channel:
        stub = service_pb2_grpc.AddServiceStub(channel)
        print("Sending request now...")
        response = stub.Multiply(service_pb2.Request(a=5, b=4))
        print(f"Response is: {response}")

if __name__ == '__main__':
    logging.basicConfig()
    run()