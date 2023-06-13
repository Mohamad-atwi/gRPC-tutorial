import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:23456') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)

        request_iterator = [
            calculator_pb2.Request(operand1=10, operand2=5, operation='+'),
            calculator_pb2.Request(operand1=10, operand2=5, operation='-'),
            calculator_pb2.Request(operand1=10, operand2=5, operation='*'),
            calculator_pb2.Request(operand1=10, operand2=5, operation='/'),
            calculator_pb2.Request(operand1=10, operand2=5, operation='^'),
        ]

        responses = stub.Calculate(iter(request_iterator))

        for response in responses:
            if response.error_message:
                print("Error:", response.error_message)
            else:
                print("Result:", response.result)

if __name__ == '__main__':
    run()
