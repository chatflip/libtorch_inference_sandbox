cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(custom_ops)

find_package(Torch REQUIRED)

add_executable(test_load_model test_load_model.cpp)
target_link_libraries(test_load_model "${TORCH_LIBRARIES}")
set_property(TARGET test_load_model PROPERTY CXX_STANDARD 14)