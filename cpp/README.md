## Install

## Requirements
- Ubuntu 18.04  

### LibTorch
```bash
wget https://download.pytorch.org/libtorch/cu111/libtorch-cxx11-abi-shared-with-deps-1.9.1%2Bcu111.zip
unzip libtorch-cxx11-abi-shared-with-deps-1.9.1+cu111.zip
```

### Cmake
```bash
wget https://github.com/Kitware/CMake/releases/download/v3.21.3/cmake-3.21.3.tar.gz
tar zxvf cmake-3.21.3.tar.gz
cd cmake-3.21.3
./bootstrap
make -j$(nproc)
sudo make install
```

## Usage
```bash
cd test_load_model
bash build.sh
cd build
./test_load_model ./../../../models/mobilenetv2.pt
./test_load_model ./../../../models/quantize_mobilenetv2.pt
./test_load_model ./../../../models/deeplabv3_mobilenetv3_large.pt
```