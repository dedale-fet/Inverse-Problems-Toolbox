#!/usr/bin/env python

from distutils.core import setup

setup(
      name='pySparseCoupledDL',
      packages=['SparseCoupledDL'],
      version='1.0',
      description='pyRestoreManifold including C++ wrappers',
      author='Konstantina Fotiadou, Greg Tsagkatakis, Nancy Panousopoulou (encapsulation by Florent Sureau)',
      author_email='kfot@ics.forth.gr',
      long_description=open('README.md').read(),
      platforms=['posix','mac os'],
      classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        ],
     )

