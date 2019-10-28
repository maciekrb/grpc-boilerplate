==================
Greeter Sample API
==================

A sample gRPC API structure in python.

This API service is build as a standalone python module. Please install doing: 

.. code-block:: console

  pip install -e .


Use the ``greeterapi --help`` to get help about options running the command.

The folder contains a package repo along with unit test structure via `nox`_.
Current configuration runs unit and system tests if defined, does linting
via `flake8`, code coverage via `pytest-cov`_ and code linting using `Black`_.

Run the sample tests:

.. code-block:: console

  $ nox



.. _nox: https://nox.thea.codes/en/stable/
.. _pytest-cov: https://pypi.org/project/pytest-cov/
.. _Black: https://github.com/psf/black

