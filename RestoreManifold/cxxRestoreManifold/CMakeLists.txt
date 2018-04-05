cmake_minimum_required(VERSION 2.8)

include(ExternalProject)
include(FindPkgConfig)

# Adding customized cmake module
list(APPEND CMAKE_MODULE_PATH  "${CMAKE_SOURCE_DIR}/cmake/Modules/")

project(ManiMRCxx)

set(Boost_USE_STATIC_LIBS        OFF) # only find static libs
set(Boost_USE_MULTITHREADED      ON)

# Find required packages
find_package(Boost REQUIRED COMPONENTS python)
find_package(PythonInterp REQUIRED)
find_package(PythonLibsNew REQUIRED)
find_package(OpenMP)

message( STATUS "C COMPILER=${CMAKE_C_COMPILER}" )
message( STATUS "OpenMP FOUND =${OpenMP_CXX_FOUND}" )
message( STATUS "OpenMP LIBS=${OpenMP_CXX_LIBRARIES}" )
message( STATUS "OpenMP FLAGS=${OpenMP_CXX_FLAGS}" )

pkg_check_modules(GSL REQUIRED gsl)
pkg_check_modules(CFITSIO REQUIRED cfitsio)

add_definitions(-DBOOST_PYTHON_STATIC_LIB)

# Downloads and compiles the Boost.NumPy package
# The library and include files are located in the build/extern directory
ExternalProject_Add(BoostNumpy
    GIT_REPOSITORY https://github.com/ndarray/Boost.NumPy
    CMAKE_ARGS  -DLIBRARY_TYPE=STATIC -DBoost_USE_STATIC_LIBS=OFF
                -DCMAKE_C_COMPILER=${CMAKE_C_COMPILER}
                -DCMAKE_CXX_COMPILER=${CMAKE_CXX_COMPILER}
                -DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR}/extern
    BINARY_DIR ${CMAKE_BINARY_DIR}/extern
    INSTALL_DIR ${CMAKE_BINARY_DIR}/extern
)
set(BoostNumpy_INCLUDE_DIRS ${CMAKE_BINARY_DIR}/extern/include)
set(BoostNumpy_LIBRARY_DIRS ${CMAKE_BINARY_DIR}/extern/lib64)
set(BoostNumpy_LIBRARIES -lboost_numpy)

if(APPLE)
    set(CMAKE_MACOSX_RPATH 1)
endif(APPLE)

# Define include and library directories
include_directories(
  ${GSL_INCLUDE_DIRS}
  ${PYTHON_INCLUDE_DIRS}
  ${Boost_INCLUDE_DIRS}
  ${BoostNumpy_INCLUDE_DIRS}
  ${CFITSIO_INCLUDE_DIRS}
)
link_directories(${BoostNumpy_LIBRARY_DIRS} ${GSL_LIBRARY_DIRS} ${CFITSIO_LIBRARY_DIRS})

# Compilation flags
#if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
#  # using Clang, disabling OpenMP support
#  set(CMAKE_CXX_FLAGS "-O3 -fomit-frame-pointer -fno-common -fPIC")
#else()
#  set(CMAKE_CXX_FLAGS "-O3 -fomit-frame-pointer -fno-common -fPIC -fopenmp")
#endif()

set(CMAKE_CXX_FLAGS "-O3 -fomit-frame-pointer -fno-common -fPIC ${OpenMP_CXX_FLAGS}")

# Build the tools module
add_library(ManiMR SHARED sparse2d/cxx/ManiMR.cpp sparse2d/cxx/starlet2d.cpp sparse2d/cxx/MRM2d.cpp)
add_dependencies(ManiMR BoostNumpy)
target_link_libraries(ManiMR ${BoostNumpy_LIBRARIES} ${Boost_LIBRARIES} ${GSL_LIBRARIES} ${PYTHON_LIBRARIES})
set_target_properties(ManiMR PROPERTIES SUFFIX .so)
set_target_properties(ManiMR PROPERTIES PREFIX "")

add_library(starlet2d SHARED sparse2d/cxx/sparse2d.cpp sparse2d/cxx/starlet2d.cpp)
add_dependencies(starlet2d BoostNumpy)
target_link_libraries(starlet2d ${BoostNumpy_LIBRARIES} ${Boost_LIBRARIES} ${GSL_LIBRARIES} ${PYTHON_LIBRARIES})
set_target_properties(starlet2d PROPERTIES SUFFIX .so)
set_target_properties(starlet2d PROPERTIES PREFIX "")

install(TARGETS ManiMR DESTINATION ${CMAKE_SOURCE_DIR}/../pyRestoreManifold/wrappers)
install(TARGETS starlet2d DESTINATION ${CMAKE_SOURCE_DIR}/../pyStarlet)
