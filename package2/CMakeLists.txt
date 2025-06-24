cmake_minimum_required(VERSION 3.22..3.27 FATAL_ERROR)
project(Package2)

find_package(package1 REQUIRED)

include(GNUInstallDirs)

add_library(package2 INTERFACE)
add_library(package2::package2 ALIAS package2)

target_include_directories(package2 
    INTERFACE 
        $<BUILD_INTERFACE:include>
        $<INSTALL_INTERFACE:include>
)

target_link_libraries(package2 INTERFACE package1::package1)

install(
    DIRECTORY include/
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

install(
      TARGETS 
         package2
      EXPORT 
         package2-targets
      ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
      LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
      RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

install(
    EXPORT package2-targets
    FILE package2-targets.cmake
    NAMESPACE package2::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

install(FILES "package2-config.cmake" DESTINATION ${CMAKE_INSTALL_LIBDIR})