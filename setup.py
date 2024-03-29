from setuptools import find_packages, setup


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'stock-prices-forecaster'
DESCRIPTION = "Stock prices forecaster package."
URL = "https://github.com/BrianKoblinc/stock-prices-forecaster"
EMAIL = "briankoblinc@gmail.com"
AUTHOR = "BrianKoblinc"
REQUIRES_PYTHON = ">=3.6.0"


long_description = DESCRIPTION

# Load the package's VERSION file as a dictionary.
about = {}
ROOT_DIR = Path("/Users/bkoblinc/Desktop/Otros proyectos/stock-prices/stock-prices-forecaster")
DATASET_DIR = ROOT_DIR.joinpath("datasets")
TRAINED_MODEL_DIR = ROOT_DIR.joinpath("trained_models")
FITTED_SCALERS_DIR = ROOT_DIR.joinpath("fitted_scalers")

ROOT_DIR = Path("/Users/bkoblinc/Desktop/Otros proyectos/stock-prices/stock-prices-forecaster")
REQUIREMENTS_DIR = ROOT_DIR.joinpath("requirements")
PACKAGE_DIR = ROOT_DIR.joinpath("models/forecaster")
with open(PACKAGE_DIR.joinpath("VERSION")) as f:
    _version = f.read().strip()
    about["__version__"] = _version


# What packages are required for this module to be executed?
def list_reqs(fname="requirements.txt"):
    with open(REQUIREMENTS_DIR / fname) as fd:
        return fd.read().splitlines()

setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    package_data={"forecaster": ["VERSION"]},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    license="BSD-3",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
