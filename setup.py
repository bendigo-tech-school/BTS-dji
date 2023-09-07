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
    name="BTS-dji",
    version="0.1.10",
    description="A simplified version of the dji robomaster library with some addons. Made for the bendigo tech school.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bendigo-tech-school/BTS-dji",
    author="Bevan Matsacos",
    author_email="B.Matsacos@latrobe.edu.au",
    license="MIT",
    classifiers=[
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 11"
    ],
    packages=["BTS-dji"],
    include_package_data=True,
    install_requires=[
        'numpy >= 1.18',
        'opencv-python >= 4.2',
        'netaddr >= 0.8',
        'netifaces >= 0.10',
        'myqr >= 2.3',
        'pynput==1.7.6',
        'robomaster==0.1.1.68',
    ]
)
