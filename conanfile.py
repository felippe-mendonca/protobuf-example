
from conans import ConanFile, CMake, tools

class ProtobufExampleConan(ConanFile):
    name = "protobuf-example"
    version = "0.0.1"
    license = "MIT"
    url = ""
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "build_tests": [True, False],
    }
    default_options = "shared=True", "fPIC=True", "build_tests=False"
    generators = "cmake", "cmake_find_package", "cmake_paths", "virtualrunenv"
    requires = (
        "protobuf/3.6.1@bincrafters/stable",
        "protoc_installer/3.6.1@bincrafters/stable",
    )
    exports_sources = "*"

    def build_requirements(self):
        pass

    def configure(self):
        self.options["protobuf"].shared = True

    def build(self):
        cmake = CMake(self, generator='Ninja')
        cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        cmake.configure()
        cmake.build()

    def package_info(self):
        self.cpp_info.libs = ["protobuf-example"]