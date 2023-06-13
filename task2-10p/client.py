import grpc
import calculator_pb2
import calculator_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:23456') as channel:
    # some call examples here

if __name__ == '__main__':
    run()
