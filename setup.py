#!/usr/bin/env python3

from setuptools import setup
from setuptools import find_packages

import pfc


setup(
    name="pfc",
    version=pfc.__version__,

    packages=find_packages(),

    author="d0p1",
    author_email="d0p1@yahoo.com",

    description="Tiny FORTRAN I Compiler writen in python",
    long_description=open("README.md").read(),

    url="https://github.com/d0p1s4m4/FORTRAN-Compiler",

    classifiers=[
        "Environment :: Console",
        "License :: Other/Proprietary License",
        "Natural Language :: English",
        "Natural Language :: French",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Fortran",
        "Topic :: Software Development :: Compilers"
    ],

    entry_points={
        'console_scripts': [
            'pfc = pfc.entry:main'
        ]
    },
    license="Beerware"
)