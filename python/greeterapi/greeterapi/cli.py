"""
Command line::
greeterapi -- CLI to Greeter gRPC Service

Usage:
     greeterapi server
        [--dataflow-param-runner=NAME]
        [--host=HOST]
        [--loglevel=LEVEL]
        [--max-workers=NUM]
        [--shutdown-grace=NUM]
        [--no-ssl]

Options:
    -h --help                              Show help screen.
    --host=HOST                            Service host [default: localhost:50001].
    --loglevel=LEVEL                       The desired log level for the server to run [default: INFO].
    --max-workers=NUM                      Max workers in thread pool executor [default: 1].
    --no-ssl                               Create an insecure channel instead of a secure one.
    --shutdown-grace=NUM                   Number of grace seconds when shutdown is started [default: 0].
    --version                              Show version.
"""

import logging
import sys
import time
from concurrent import futures
from docopt import docopt
import grpc

from myproject.proto.greeter.v1 import service_pb2_grpc
import greeterapi.v1.servicer
from . import __version__


def main():
    """ Main CLI entrypoint. """

    args = docopt(__doc__, version=__version__.__version__)

    if ":" not in args["--host"]:
        print("--host has to be in the form host:port", file=sys.stderr)
        raise SystemExit(1)

    numeric_level = getattr(logging, args["--loglevel"].upper(), None)
    if not isinstance(numeric_level, int):
        logging.error("Invalid --loglevel: %s", args["--loglevel"])
        raise SystemExit(1)

    logging.basicConfig(
        format="[%(asctime)s.%(msecs)03d] %(levelname)s %(name)s:%(lineno)d %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
        level=numeric_level,
    )

    host, port = args["--host"].split(":")

    pool = futures.ThreadPoolExecutor(max_workers=int(args["--max-workers"]))
    grpc_server = grpc.server(pool)

    # Multiple versions of the API can be served by the gRPC server
    # v1 servicer is configured here
    v1_svc = greeterapi.v1.servicer.GreeterService()
    service_pb2_grpc.add_GreeterServicer_to_server(v1_svc, grpc_server)

    grpc_server.add_insecure_port("[::]:" + port)
    print("Starting gRPC Greeter Service v{}".format(__version__.__version__))
    grpc_server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)  # one day in seconds
    except KeyboardInterrupt:
        print("Shutting down gRPC Server, good bye !!")
        grpc_server.stop(int(args["--shutdown-grace"]))


if __name__ == "__main__":
    main()
