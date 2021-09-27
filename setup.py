from setuptools import setup
# from version import get_version
setup(
    name='pysleep',
    version='0.1',
    author='hyu81',
    author_email='hyu81@gatech.edu',
    description='Python package for sleep stage classification',
    packages=['pysleep'],
    install_requires=[
        'numpy',
    ],
)