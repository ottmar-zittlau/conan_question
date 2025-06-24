from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import copy

class Package(ConanFile):
    settings = "build_type"

    name = "package1"
    version = "0.0.0"

    def requirements(self):
        self.requires("magic_enum/0.9.7", transitive_headers=True)
        # self.requires("spdlog/1.15.3")

    
    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()
    
    def layout(self):
        cmake_layout(self)

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def export_sources(self):
        copy(self, "CMakeLists.txt", self.recipe_folder, self.export_sources_folder)
        copy(self, "package1-config.cmake", self.recipe_folder, self.export_sources_folder)
        copy(self, "include/*", self.recipe_folder, self.export_sources_folder)

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "none")
        self.cpp_info.builddirs.append("lib")