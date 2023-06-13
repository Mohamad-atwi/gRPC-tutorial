# client.py
import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():
    print("Running client say hello")
    with grpc.insecure_channel('localhost:12345') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        request = helloworld_pb2.Request(name='John')
        response = stub.SayHello(request)
    print("Client received: " + response.message)

if __name__ == '__main__':
    run()
