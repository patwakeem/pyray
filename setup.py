#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='pyray',
    version='2016.3.12',
    description='A python client to interact with the Riverbed Stingray REST API.',
    long_description=readme + '\n\n' + history,
    author='Originally by: Matt Welch, Forked by: Patrick W.',
    author_email='mwelch@tallshorts.com,patwakeem@gmail.com',
    url='https://github.com/patwakeem/pyray',
    packages=[
        'pyray',
    ],
    package_dir={'pyray': 'pyray'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='pyray',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)