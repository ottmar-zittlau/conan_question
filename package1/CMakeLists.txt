cmake_minimum_required(VERSION 3.22..3.27 FATAL_ERROR)
project(Package1)

include(GNUInstallDirs)

add_library(package1 INTERFACE)
add_library(package1::package1 ALIAS package1)

target_include_directories(package1 
    INTERFACE 
        $<BUILD_INTERFACE:include>
        $<INSTALL_INTERFACE:include>
)

target_link_libraries(package1 INTERFACE magic_enum::magic_enum)

install(
    DIRECTORY include/
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

install(
      TARGETS 
         package1
      EXPORT 
         package1-targets
      ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
      LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
      RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

install(
    EXPORT package1-targets
    FILE package1-targets.cmake
    NAMESPACE package1::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

install(FILES "package1-config.cmake" DESTINATION ${CMAKE_INSTALL_LIBDIR})