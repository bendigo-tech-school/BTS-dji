# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="BTS_dji",
    version="0.1.5",
    description="A simplified version of the dji robomaster library with some addons. Made for the bendigo tech school.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author="Bevan Matsacos",
    author_email="B.Matsacos@latrobe.edu.au",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["BTS_dji"],
    include_package_data=True,
    install_requires=["pynput", "robomaster"]
)