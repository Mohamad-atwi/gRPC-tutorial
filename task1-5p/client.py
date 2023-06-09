import grpc
import helloworld_pb2
import helloworld_pb2_grpc


def run():
    print("Run client say hello ")
    with grpc.insecure_channel('localhost:12345') as channel:
        #client
        stub = #create stub from helloworld_pb2_grpc
        response = # use stub to send req and get resp from server
    print("Client received: " + response.message)

if __name__ == '__main__':
    run()

