from setuptools import setup, find_packages
import os

# # Utility function to parse requirements.txt
# def parse_requirements(filename):
#     """ Load requirements from a pip requirements file """
#     with open(filename, 'r') as f:
#         return [line.strip() for line in f if line and not line.startswith("#")]

# # Path to the requirements.txt file
# requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')

# Read the requirements from the requirements.txt file
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="reporting_optr",
    version="0.1",
    description="A reporting package for OPTR project",
    packages=find_packages(),
    install_requires=required,  # Dynamically load from requirements.txt
)
