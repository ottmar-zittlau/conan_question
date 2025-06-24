include(CMakeFindDependencyMacro)

# find_dependency(spdlog REQUIRED)
find_dependency(magic_enum REQUIRED)

include(${CMAKE_CURRENT_LIST_DIR}/package1-targets.cmake)