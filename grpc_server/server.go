package main

import (
	"context"
	"log"
	"net"
	"proto"

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
	proto.RegisterAddServiceServer(srv, &server{})
	reflection.Register(srv)
	log.Printf("gRPC Server is running now. Waiting for requests...")
	e := srv.Serve(listener)
	if e != nil {
		panic(e)
	}

}

func (s *server) Add(ctx context.Context, request *proto.Request) (*proto.Response, error) {
	a, b := request.GetA(), request.GetB()
	result := a + b
	log.Printf("Received request for adding numbers: %d + %d = %d", a,b, result)
	return &proto.Response{Result: result}, nil
}

func (s *server) Multiply(ctx context.Context, request *proto.Request) (*proto.Response, error) {
	a, b := request.GetA(), request.GetB()
	result := a * b
	log.Printf("Received request for multiply numbers: %d * %d = %d", a,b, result)
	return &proto.Response{Result: result}, nil
}
