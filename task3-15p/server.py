from concurrent import futures
import grpc
import calculator_pb2
import calculator_pb2_grpc

class Calculator(calculator_pb2_grpc.CalculatorServicer):
    def Calculate(self, request_iterator, context):
        for request in request_iterator:
            response = calculator_pb2.Response()
            if request.operation == '+':
                response.result = request.operand1 + request.operand2
            elif request.operation == '-':
                response.result = request.operand1 - request.operand2
            elif request.operation == '*':
                response.result = request.operand1 * request.operand2
            elif request.operation == '/':
                if request.operand2 == 0:
                    response.error_message = "Division by zero error"
                else:
                    response.result = request.operand1 // request.operand2
            elif request.operation == '^':
                response.result = request.operand1 ** request.operand2
            else:
                response.error_message = "Invalid operation"

            yield response

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
