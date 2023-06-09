generate gRPC classes:
python -m grpc_tools.protoc -I ./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/calculator.proto

run your server and client:

python server.py
python client.py

Your second task is to create server with gRPC that perform some math tasks:

addition, subtraction, multiplication, division and exponentiation

remember to return error from server e.g. while divided by zero
