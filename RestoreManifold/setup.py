#!/usr/bin/env python

from distutils.core import setup

setup(
      name='pyRestoreManifold',
      packages=['pyRestoreManifold','pyRestoreManifold.restore','pyRestoreManifold.trans','pyRestoreManifold.utils','pyRestoreManifold.wrappers'],
      version='1.0',
      license = "CeCILL",
      description='pyRestoreManifold including C++ wrappers',
      author='Jerome Bobin (encapsulation by Florent Sureau)',
      author_email='jerome.bobin@cea.fr',
      long_description=open('README.md').read(),
      platforms=['posix','mac os'],
      classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "License :: CeCILL FREE SOFTWARE LICENSE",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        ],
     )

setup(
      name='pyStarlet',
      packages=['pyStarlet'],
      version='1.0',
      license = "CeCILL",
      description='pyStarlet including C++ wrappers',
      author='Jerome Bobin (encapsulation by Florent Sureau)',
      author_email='jerome.bobin@cea.fr',
      long_description=open('README.md').read(),
      platforms=['posix','mac os'],
      classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "License :: CeCILL FREE SOFTWARE LICENSE",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        ],
     )
