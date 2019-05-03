protoc --proto_path=proto --proto_path=/usr/local/opt/protoc-3.7.1-osx-x86_64/include --go_out=plugins=grpc:proto service.proto

if [ $? -ne 0 ]; then
    echo "ERROR while creating go stub file!"
    exit 1
fi

echo "Go stub file successfully created..."
ls -rtl proto/service.pb.go

