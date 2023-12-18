# TestConanClion

## Build from command line
```shell
# create build folder
mkdir build && cd build
# get conan generate linux clang-5 makefiles and build dependencies:
conan install .. -pr=linux_x86_64-clang5 --build=missing
# configure cmake
conan build .. --configure
# build
conan build ..
```
