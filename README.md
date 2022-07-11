# TestConanClion

## Build from command line
```shell
# create build folder
mkdir build && cd build
# get conan generate linux clang-12 makefiles and build dependencies:
conan install .. -pr=linux_x86_64-clang12 --build=missing
# configure cmake
conan build .. --configure
# build
conan build ..
```
