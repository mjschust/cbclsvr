#Dependencies
```
go: google.golang.org/grpc, github.com/golang/protobuf/protoc-gen-go
python: grpcio, grpcio-tools
```

#Protobuf build commands
```
protoc -I proto/ proto/cblocks.proto --go_out=plugins=grpc:cbserver/cbservice
python -m grpc_tools.protoc -I ./proto/ --python_out=./cbclient/ --grpc_python_out=./cbclient/ ./proto/cblocks.proto
```

#Run commands
All commands should be run from the top-level directory

##Start server
`go run ./cbserver`

##Run example script
`PYTHONPATH=cbclient python -m examples.*`


