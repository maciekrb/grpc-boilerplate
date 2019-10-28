""" sampleapis package """

import setuptools

install_requires = ["protobuf >= 3.6.0, < 4.0", "grpcio>=1.20.1"]

extras_require = {}

setuptools.setup(
    name="sampleapis",
    version="0.0.0",  # Replaced by sed when running package_protos.sh
    author="Jhon Doe",
    author_email="jhon@example.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    description="Python generated classes for sampleAPIs",
    long_description="Protobuf message definition for SampleAPIs",
    install_requires=install_requires,
    extras_require=extras_require,
    license="GPLv3",
    namespace_packages=["myproject"],
    packages=setuptools.find_packages(),
)
