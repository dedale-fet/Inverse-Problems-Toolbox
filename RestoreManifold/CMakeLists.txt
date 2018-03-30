cmake_minimum_required(VERSION 2.8)

include(ExternalProject)
include(FindPkgConfig)

project(restoreManifold)

find_package(PythonInterp 2.7 REQUIRED)

ExternalProject_Add(ManiMRCxx
    SOURCE_DIR  ${CMAKE_SOURCE_DIR}/cxxRestoreManifold
    CMAKE_ARGS    -DCMAKE_C_COMPILER=${CMAKE_C_COMPILER}
                  -DCMAKE_CXX_COMPILER=${CMAKE_CXX_COMPILER}
                  -DCMAKE_MODULE_PATH=${CMAKE_MODULE_PATH}
                  -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    BINARY_DIR  ${CMAKE_SOURCE_DIR}/cxxRestoreManifold/build
)

#
# Install python libraries
#
add_custom_target(install_python ALL ${PYTHON_EXECUTABLE} setup.py install
    --prefix=${CMAKE_INSTALL_PREFIX} WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
add_dependencies(install_python ManiMRCxx)

install(FILES pyRestoreManifold/wrappers/ManiMR.so DESTINATION ${CMAKE_INSTALL_PREFIX}/lib/python2.7/site-packages/pyRestoreManifold/wrappers)
install(FILES pyStarlet/sparse2d_Sn.so DESTINATION ${CMAKE_INSTALL_PREFIX}/lib//python2.7/site-packages/pyStarlet)
