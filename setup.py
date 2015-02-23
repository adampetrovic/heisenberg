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

setup(
    name='heisenberg-ec2',
    version='1.0.3',
    description='A utility for searching and connecting to EC2 instances with caching for quicker interaction',
    author='Adam Petrovic',
    author_email='adam@petrovic.com.au',
    url='https://github.com/adampetrovic/heisenberg',
    download_url='https://github.com/adampetrovic/heisenberg/tarball/1.0.3',
    packages=[
        'heisenberg',
        'heisenberg.command',
    ],
    scripts=['bin/ec2'],
    include_package_data=True,
    install_requires=[
        'boto',
        'texttable',
    ],
    zip_safe=False,
    keywords='heisenberg',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
