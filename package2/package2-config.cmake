include(CMakeFindDependencyMacro)
find_dependency(package1 REQUIRED)

include(${CMAKE_CURRENT_LIST_DIR}/package2-targets.cmake)