# pyRestoreManifold

## **Toolbox for solving restoration problems for manifold-valued data**

***

This toolbox is composed of the following submodules:

***


***

### **Pre-Requirements to compile C++ wrappers**

***

For compilation of C++ sources, the following libraries are required:

- cmake (tested with 3.8.1)
- boost (tested with 1.64.0), python library
- python2 (tested with 2.7.13)
- gsl (tested with 2.2.1)
- cfistio (tested with 3.31)

To compile the wrappers, go to ${ROOT_pyRestoreManifold}/wrappers/sources/build
where ${ROOT_pyRestoreManifold} is the root of the package and type `cmake ../`

If you have multiple C++ compilers or python compilers installed on your machine,
ensure that you select the correct set used for building the other libraries (boost in particular).
This can be done with the following options:

```Shell
cmake ../ -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++
```
