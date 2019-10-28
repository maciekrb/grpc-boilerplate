#!/bin/bash
# Generates Python classes around proto messages as a namespaced
# package: myproject.proto

# Exit on error
set -e


PYTHON=$(which python)
PROTOC=protoc
VERSION=$1
PROTO_FILES=../../sampleapis
OUT_PATH=../proto-build

is_osx () {
  [[ $('uname') == 'Darwin' ]]
}

if is_osx; then
  SED=$(which gsed)
else
  SED=$(which sed)
fi

if [ "$SED" = "" ]; then
  echo "Could not find sed :-/"
  exit 1
fi

if [ "$PYTHON" = '' ]; then
  echo "A python executable is required to build python protos"
fi

if [ "$VERSION" = '' ]; then
  echo "Please specify a version as the first positional argument. ie. 0.0.20"
  exit 1
fi

# Clean up
echo "Cleaning up ..."
rm -rf $OUT_PATH
mkdir -p $OUT_PATH

echo "Using python: $PYTHON"
echo "Building python proto package v${VERSION} ..."
echo "Searching for protobuf compiler ..."
# Generate protos
# make sure you did pip install grpcio grpcio-tools
TARGET_PROTOS=$(find $PROTO_FILES -name "*.proto")

echo "Using python grpc.tools.protoc"
python -m grpc.tools.protoc \
  --proto_path $PROTO_FILES \
  --python_out=$OUT_PATH \
  --grpc_python_out=$OUT_PATH \
  --include_imports \
  --descriptor_set_out sampleapis_descriptors.pb \
  $TARGET_PROTOS

# Add proto namespace
mkdir $OUT_PATH/proto
mv $OUT_PATH/myproject/* $OUT_PATH/proto
mv $OUT_PATH/proto $OUT_PATH/myproject

# Adjust python imports to namespaced package structure
GEN_FILES=$(find $OUT_PATH/myproject -name "*.py")
$SED -i 's@import myproject\.@import myproject.proto.@g' $GEN_FILES
$SED -i 's@from myproject\.@from myproject.proto.@g' $GEN_FILES

# add __init__.py namespace files
echo "__import__('pkg_resources').declare_namespace(__name__)" \
  > $OUT_PATH/myproject/__init__.py

# Add __init__.py files to every produced folder
find $OUT_PATH/myproject/proto -type d -exec touch {}/__init__.py \;

cp setup.py README.rst $OUT_PATH
$SED -i "s@version=\"0.0.0\"@version='${VERSION}'@" $OUT_PATH/setup.py
cd $OUT_PATH && $PYTHON setup.py sdist
