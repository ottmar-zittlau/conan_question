cmake_minimum_required(VERSION 3.22..3.27 FATAL_ERROR)
project(Package2)

include(GNUInstallDirs)

install(FILES "package2-config.cmake" DESTINATION ${CMAKE_INSTALL_LIBDIR})