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
    name='heisenberg',
    version='0.1',
    description='A utility for searching and connecting to EC2 instances',
    author='Adam Petrovic',
    author_email='adam@freelancer.com',
    url='https://gitlab.freelancer.com/adam/heisenberg',
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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
