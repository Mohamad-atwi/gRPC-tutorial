import grpc
import helloworld_pb2
import helloworld_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:34567') as channel:
    # some call examples here

if __name__ == '__main__':
    run()