from conan import ConanFile
from conan.tools.cmake import CMake


class CompressorRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("zlib/1.2.11")

    def build_requirements(self):
        self.tool_requires("cmake/[^3.23]")
        
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()