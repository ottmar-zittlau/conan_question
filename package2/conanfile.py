from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import copy

import os

class Package(ConanFile):
    settings = "build_type"

    name = "package2"
    version = "0.0.0"

    def requirements(self):
        self.requires("package1/0.0.0")
        # If I repeat the dependency here, it works...
        # self.requires("magic_enum/0.9.7", transitive_headers=True)

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
        copy(self, "package2-config.cmake", self.recipe_folder, self.export_sources_folder)
        copy(self, "include/*", self.recipe_folder, self.export_sources_folder)

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "none")
        self.cpp_info.builddirs.append(os.path.join("lib"))

