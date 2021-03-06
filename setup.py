from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='otp-transit-analysis',
    version='0.0.0',
    description='transit analysis',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    test_suite="tests",
)
