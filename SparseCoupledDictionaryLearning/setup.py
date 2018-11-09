#!/usr/bin/env python

from distutils.core import setup

setup(
      name='pySparseCoupledDL',
      packages=['SparseCoupledDL'],
      version='1.0',
      license="Copyright (c) 2017-2018, Signal Processing Lab (SPL), Institute of Computer Science (ICS), FORTH, Greece.",
      description='Coupled Dictionary Learning using sparsity',
      author='Konstantina Fotiadou, Greg Tsagkatakis, Nancy Panousopoulou (encapsulation by Florent Sureau)',
      author_email='kfot@ics.forth.gr',
      long_description=open('README.md').read(),
      platforms=['posix','mac os'],
      classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
	"License :: Copyright (c) 2017-2018, Signal Processing Lab (SPL), Institute of Computer Science (ICS), FORTH, Greece.",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        ],
     )

