# **Description of Dedale Toolbox**

This toolbox contains two packages that were designed in the context of workpackage 3 of the DEDALE FET-OPEN project (<http://dedale.cosmostat.org>):

- SparseCoupledDictionaryLearning is a package authored by Konstantina Fotiadou, Greg Tsagkatakis, Nancy Panousopoulou from FORTH institute. The purpose of this software is to perform spectral super-resolution in a coupled dictionary learning framework using sparsity.

- RestoreManifold is a package authored by Jérome Bobin (CEA), that allows to solve some restoration problems (denoising, inpainting) for manifold-valued data.

Three python notebooks illustrate how to use these  packages. See the documentation in each package for more details


***

### **Pre-Requirements to compile RestoreManifold (C++ wrappers)**

***

For compilation of C++ sources, the following libraries are required:

- cmake (tested with 3.8.1)
- boost (tested with 1.64.0), python library
- python2.7 (tested with 2.7.13)
- gsl (tested with 2.2.1)
- cfistio (tested with 3.31)

To compile the wrappers, go to ${ROOT_DEDALE_TOOLBOX}/build
where ${ROOT_DEDALE_TOOLBOX} is the root of the toolbox and type `cmake ../`

If you have multiple C++ compilers or python compilers installed on your machine,
ensure that you select the correct set used for building the other libraries (boost in particular).
This can be done with the following options:

```Shell
cmake ../ -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++
```


At the end of the compilation, all python libraries will be installed in directory
`${ROOT_DEDALE_TOOLBOX}/install/lib/python2.7/site-packages`
