=========================
API Definition repository
=========================

This repository contains the interface definitions of the Company's APIs over the
`gRPC`_ protocol. The original interface definitions and their corresponding
documentation should provide the central documentation for developers building
client applications.

It is a good practice to create specific language packages using these definitions
so it's easy for others to build applications around specific versions of the `Protocol
buffer`_ files.


Consider `Google's API design guide <https://cloud.google.com/apis/design/standard_fields>`_ 
for over all best practices when desing APIs.

Consider using `ESP`_ or `Envoy`_ tooling to transcode and overhaul your API implementations.



The structure of the repository is based on `Google's own service repository <https://github.com/googleapis/googleapis>`_ 
for gRPC services.


.. _gRPC: https://grpc.io
.. _Protocol buffers: https://github.com/google/protobuf
.. _Envoy: https://github.com/tetratelabs/istio-tools/tree/master/grpc-transcoder
.. _ESP: https://github.com/cloudendpoints/esp
