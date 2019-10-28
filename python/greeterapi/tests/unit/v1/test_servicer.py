import unittest

import grpc
from grpc.framework.foundation import logging_pool

from myproject.proto.greeter.v1 import service_pb2
from myproject.proto.greeter.v1 import service_pb2_grpc
import greeterapi.v1.servicer


class TestServicerV1(unittest.TestCase):
    def setUp(self):
        self._server_pool = logging_pool.pool(1)
        self._grpc_server = grpc.server(self._server_pool)

        # Multiple versions of the API can be served by the gRPC server
        # v1 servicer is configured here
        v1_svc = greeterapi.v1.servicer.GreeterService()
        service_pb2_grpc.add_GreeterServicer_to_server(v1_svc, self._grpc_server)

        port = self._grpc_server.add_insecure_port("[::]:0")
        self._grpc_server.start()

        # Create the client stub
        channel = grpc.insecure_channel("localhost:%d" % port)
        self.grpc_stub = service_pb2_grpc.GreeterStub(channel)

    def tearDown(self):
        self._grpc_server.stop(None)
        self._server_pool.shutdown(wait=True)

    def test_servicer(self):
        res = self.grpc_stub.SayHello(service_pb2.HelloRequest(name="Jhon"))
        self.assertEqual("Hello, Jhon!", res.message)
