#!/bin/bash
export LIBTORCH_ROOT="./../libtorch"
rm -rf build
mkdir build
cd build
cmake -DCMAKE_PREFIX_PATH=${LIBTORCH_ROOT} ..
cmake --build . --config Release
