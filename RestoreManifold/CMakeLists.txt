cmake_minimum_required(VERSION 2.8)

include(ExternalProject)
include(FindPkgConfig)

project(restoreManifold)

message(STATUS "restoreManif:CSD=${CMAKE_SOURCE_DIR}" )

ExternalProject_Add(ManiMRCxx
    SOURCE_DIR  ${CMAKE_SOURCE_DIR}/cxxRestoreManifold            # Source dir to be used for build
    CMAKE_ARGS    -DCMAKE_C_COMPILER=${CMAKE_C_COMPILER}
                  -DCMAKE_CXX_COMPILER=${CMAKE_CXX_COMPILER}
                  -DCMAKE_MODULE_PATH=${CMAKE_MODULE_PATH}
    BINARY_DIR  ${CMAKE_SOURCE_DIR}/cxxRestoreManifold/build
)

#
# Install python libraries
#
#INSTALL(TARGETS pytools_pisap DESTINATION ../../lib/python2.7/site-packages)
#INSTALL(TARGETS pysparse2d_pisap DESTINATION ../../lib/python2.7/site-packages)
#add_custom_target(install_python ALL python setup.py install --prefix=${PROJECT_SOURCE_DIR}/../..
#    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/python)
