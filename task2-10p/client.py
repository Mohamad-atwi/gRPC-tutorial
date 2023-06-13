import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:23456') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)

        request = calculator_pb2.Request(operand1=10, operand2=5)
        response = stub.Add(request)
        print("Addition Result:", response.result)

        request = calculator_pb2.Request(operand1=10, operand2=5)
        response = stub.Subtract(request)
        print("Subtraction Result:", response.result)

        request = calculator_pb2.Request(operand1=10, operand2=5)
        response = stub.Multiply(request)
        print("Multiplication Result:", response.result)

        request = calculator_pb2.Request(operand1=10, operand2=5)
        response = stub.Divide(request)
        print("Division Result:", response.result)

        request = calculator_pb2.Request(operand1=10, operand2=5)
        response = stub.Exponentiate(request)
        print("Exponentiation Result:", response.result)

if __name__ == '__main__':
    run()
