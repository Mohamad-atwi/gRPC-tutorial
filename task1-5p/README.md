generate gRPC classes:
python -m grpc_tools.protoc -I ./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/helloworld.proto

implement client.py and server.py

run your server and client:

python server.py
python client.py