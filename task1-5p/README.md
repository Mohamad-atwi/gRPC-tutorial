Your first task is to implement base hello world procedure.
Look on helloworld.proto there is all you need for implement server and client.

First generate gRPC classes with:
python -m grpc_tools.protoc -I ./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/helloworld.proto

then add some code in client.py and server.py to basicly run sayHello procedure and get respodn message from server

run your server and client:

python server.py
python client.py