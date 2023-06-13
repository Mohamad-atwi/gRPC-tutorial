from concurrent import futures

import grpc
import calculator_pb2
import calculator_pb2_grpc

class Calculator(calculator_pb2_grpc.CalculatorServicer):

    #def add(self, request, context):
        #return your response here


def serve():
    port = '23456'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    # addServicer_to_server
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
