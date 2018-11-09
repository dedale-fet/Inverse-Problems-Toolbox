cmake_minimum_required(VERSION 2.8)

include(ExternalProject)
include(FindPkgConfig)

project(sparseCoupledDL)

find_package(PythonInterp 2.7 REQUIRED)


#
# Install python libraries
#
add_custom_target(install_python ALL ${PYTHON_EXECUTABLE} setup.py install
    --prefix=${CMAKE_INSTALL_PREFIX} WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
