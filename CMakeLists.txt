cmake_minimum_required(VERSION 2.8)

include(ExternalProject)
include(FindPkgConfig)

# Adding customized cmake module
list(APPEND CMAKE_MODULE_PATH  "${CMAKE_SOURCE_DIR}/cmake/Modules/")

project(DedaleToolbox)

message(STATUS "DedaleToolbox:CSD=${CMAKE_SOURCE_DIR}" )

ExternalProject_Add(restoreManifold
    SOURCE_DIR  ${CMAKE_SOURCE_DIR}/RestoreManifold
    BINARY_DIR  ${CMAKE_SOURCE_DIR}/RestoreManifold/build
    INSTALL_DIR ${CMAKE_SOURCE_DIR}/install
    CMAKE_ARGS  -DCMAKE_C_COMPILER=${CMAKE_C_COMPILER}
                -DCMAKE_CXX_COMPILER=${CMAKE_CXX_COMPILER}
                -DCMAKE_MODULE_PATH=${CMAKE_MODULE_PATH}
                )
