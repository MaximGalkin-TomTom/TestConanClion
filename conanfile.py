import os
from pathlib import Path
from conans import ConanFile, CMake, errors, tools, python_requires

class TestConanClion(ConanFile):
    name = "test-conan-clion"
    settings = "os", "compiler", "build_type", "arch", "toolchain"

    requires = (
        "boost/[>=0.1.4+1.70.0]@tomtom/master"
    )

    generators = "cmake", "cmake_find_package"

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

