import logging
from myproject.proto.greeter.v1 import service_pb2
from myproject.proto.greeter.v1 import service_pb2_grpc


class GreeterService(service_pb2_grpc.GreeterServicer):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def SayHello(self, request, context):
        self.logger.debug("Calling SayHello: {}".format(request))
        return service_pb2.HelloReply(message="Hello, {}!".format(request.name))
