#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="Legendarium",
    version='0.1',
    description="Python library to handle SciELO`s bibliographic legend",
    author="Jamil Atta Junior",
    author_email="atta.jamil@gmail.com",
    license="BSD",
    url="https://github.com/scieloorg/legendarium",
    py_modules=["legendarium"],
    keywords='SciELO bibliographic legend library legendarium',
    maintainer_email='atta.jamil@gmail.com',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Customer Service",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: Portuguese (Brazilian)",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    setup_requires=[],
    tests_require=[],
    test_suite='tests'
)
