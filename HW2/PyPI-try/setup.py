from setuptools import setup, find_packages

setup(
    name='alexlatexgen',
    version='1.0',
    description='Library for generating tex files',
    package_dir = {"": "tex_gen"},
    # packages=find_packages(exclude=['PyPI-try/tex_gen']),
    author="Alexandra Durneva"
)
