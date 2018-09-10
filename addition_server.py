"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import time

import grpc

import addition_pb2
import addition_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Addition(addition_pb2_grpc.AdditionServicer):
	def SayHello(self, request, context):
		return addition_pb2.Res(name='manish here  %s !' % request.name);

	def Add(self, request, context):
		return addition_pb2.Answer(sum=(request.num1+request.num2));


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    addition_pb2_grpc.add_AdditionServicer_to_server(Addition(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()