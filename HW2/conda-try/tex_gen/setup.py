from setuptools import setup, find_packages

setup(
    name='alex_tex_generator',
    version='1.0',
    description='Library for generating tex files',
    packages=find_packages(exclude=['tex_gen']),
)
