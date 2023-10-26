cmake_minimum_required(VERSION 3.17)
project(TestConanClion)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_VERBOSE_MAKEFILE ON)

set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -fno-limit-debug-info")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

conan_check_compiler()
conan_set_find_paths()
conan_output_dirs_setup()

find_package(Boost REQUIRED)

add_executable(TestConanClion main.cpp)
target_link_libraries(TestConanClion PRIVATE Boost::headers)