# This is protoc installation on iOS and 
# protoc installtion location is here /usr/local/opt/protoc-3.7.1-osx-x86_64/ and might differ in your case !!!

protoc --proto_path=. --proto_path=/usr/local/opt/protoc-3.7.1-osx-x86_64/include --go_out=plugins=grpc:. service.proto

if [ $? -ne 0 ]; then
    echo "ERROR while creating go stub file!"
    exit 1
fi

echo "Go stub file successfully created..."
ls -rtl service.pb.go

