generate gRPC classes:
python -m grpc_tools.protoc -I ./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/calculator.proto

implement client.py and server.py

run your server and client:

python server.py
python client.py

Your last task is to improve the usage of the server from the second task with
ping-pong stream type that allow sending more data in a single procedure call.
Return error from server e.g. while divided by zero context may be helpful

if you dont know how to create an interator look on https://adityamattos.com/grpc-in-python-part-3-implementing-grpc-streaming
