# gRPC - https://grpc.io/

## _Protocol Buffers_

1. https://developers.google.com/protocol-buffers/

## _Installation_

#### Download and Install Protocol Buffer Compiler (`protoc`)

Download and install from https://github.com/protocolbuffers/protobuf/releases.

After download and unpacking zip-file to your preferred location, create a link:
```
// creating a softlink
sandbox$ ln -s /usr/local/opt/protoc-3.7.1-osx-x86_64/bin/protoc protoc
sandbox$ protoc --version
libprotoc 3.7.1.
```


#### Download and Install grpc packages

Here we are using `golang`, so we install the required `golang` packages for gRPC.

1. The main package for grpc:
`go get -u google.golang.org/grpc`

2. To use the protoc defintion and generating code out of that:
`go get -u github.com/golang/protobuf/protoc-gen-go`

Protocol Buffer Basics: Go -  https://developers.google.com/protocol-buffers/docs/gotutorial

A simple example of a protoc file looks like that:
```go
// protocol buffer sysntax version
syntax = "proto3";

package proto;

// data structure for our request
message Request {
    int64 a = 1;
    int64 b = 2;
}

// data structure for our response
message Response {
    int64 result = 1;
}

// service that handles requests and create responses
service AddService {
    rpc Add(Request) returns (Response);
    rpc Multiply(Request) returns (Response);
}
```

## Start writing `protoc` definition

* Protocol Buffer Language Guide https://developers.google.com/protocol-buffers/docs/proto
* You can use VSCode plugin https://marketplace.visualstudio.com/itemdetails?itemName=zxh404.vscode-proto3

## Compiling `protoc` defintion

Now that we have created our protoc defintion and installed the protoc compiler, we can compile proto-file to `go` code.

`sandbox$ protoc --proto_path=proto --proto_path=third_party --go_out=plugins=grpc:proto service.proto`

**See also script `run_protoc.sh` !**

This will generate a file `service.pb.go` which includes real go code. This is our API code which we now can use for our application i.e. a web service.
