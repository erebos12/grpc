package main

import (
    "context"
    "proto"
    "net"
    "google.golang.org/grpc"
    "google.golang.org/grpc/reflection"
)

type server struct{}

func main() {
    listener, err := net.Listen("tcp", ":4040")
    if err != nil {
        panic(err)
    }

    srv := grpc.NewServer()
    RegisterAddServiceServer(srv, &server{})
    reflection.Register(srv)

    if e := srv.Serve(listener); e != nil {
        panic(e)
    }

}

func (s *server) Add(ctx context.Context, request *Request) (*Response, error) {
    a, b := request.GetA(), request.GetB()

    result := a + b

    return &Response{Result: result}, nil
}

func (s *server) Multiply(ctx context.Context, request *Request) (*Response, error) {
    a, b := request.GetA(), request.GetB()

    result := a * b

    return &Response{Result: result}, nil
}