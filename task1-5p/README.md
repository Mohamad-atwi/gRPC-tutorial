Your first task is to implement the base hello world procedure.
Look on helloworld.proto there is all you need to implement 
server and client communication

First open terminal in task1-5p dir and generate gRPC classes with:
python -m grpc_tools.protoc -I ./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/helloworld.proto

then add some code in client.py and server.py to basically 
run SayHello procedure and get response message from server

run your server and client:

python server.py
python client.py