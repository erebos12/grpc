#!/usr/bin/env bash

# install grpc: "python -m pip install grpcio"
# install grpc tools: "python -m pip install grpcio-tools"

python -m grpc_tools.protoc -I../proto --python_out=. --grpc_python_out=. ../proto/service.proto