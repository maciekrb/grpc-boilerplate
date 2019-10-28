====================
Python gRPC Services
====================

This folder contains a sample Python gRPC service. 

Please make sure you become familiar with the proto definitions found
in ``sampleapis`` before following the steps below. 


Generating the Python classes
=============================

The ``tools`` folder contains a script that uses `grpcio-tools`_ to 
geenrate the Python classes from the proto definitions in ``sampleapis``. 

The script will also build a standalone python package that you can install
into the virtualenv. 

.. code-block:: console

  # Build version 0.0.01 of the package from the ../sampleapis proto definitions
  $ ./package_protos.sh 0.0.1

To use the package in your project, install the generated package:


.. code-block:: console

  $ pip install build/dist/sampleapis-0.0.1.tar.gz


To import the generated classes in your servicer code:

.. code-block:: python

  from myproject.proto.greeter.v1 import (
      service_pb2,
      service_pb2_grpc,
  )


.. _grpcio-tools: https://pypi.org/project/grpcio-tools/
