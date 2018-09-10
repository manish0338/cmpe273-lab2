from __future__ import print_function


import grpc

import addition_pb2
import addition_pb2_grpc

def run():
	with grpc.insecure_channel('localhost:50051') as channel:
		stub = addition_pb2_grpc.AdditionStub( channel )
		number1 = input("Enter 1st number:")
		number2 = input("Enter 2nd number:")
		response = stub.Add(addition_pb2.Numbers(num1=int(number1),num2=int(number2)))
		print("Addition - " + str(response.sum))

if __name__ == '__main__':
	run()