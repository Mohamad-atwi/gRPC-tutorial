from concurrent import futures
import grpc
import calculator_pb2
import calculator_pb2_grpc

class Calculator(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.operand1 + request.operand2
        return calculator_pb2.Response(result=result)

    def Subtract(self, request, context):
        result = request.operand1 - request.operand2
        return calculator_pb2.Response(result=result)

    def Multiply(self, request, context):
        result = request.operand1 * request.operand2
        return calculator_pb2.Response(result=result)

    def Divide(self, request, context):
        result = request.operand1 // request.operand2
        return calculator_pb2.Response(result=result)

    def Exponentiate(self, request, context):
        result = request.operand1 ** request.operand2
        return calculator_pb2.Response(result=result)

def serve():
    port = '23456'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
