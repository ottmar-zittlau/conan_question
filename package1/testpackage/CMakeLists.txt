cmake_minimum_required(VERSION 3.20)
project(PackageTest CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(package1 REQUIRED)

add_executable(cpp_test main.cpp)
target_link_libraries(cpp_test PRIVATE package1::package1)
