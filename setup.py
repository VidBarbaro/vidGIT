#!/usr/bin/env python3

from setuptools import setup

setup (name = 'vidGIT',
       version = '1.0',
       packages = ['vidGIT'],
       entry_points = {
           'console_scripts' : [
               'vidGIT = vidGIT.cli:main'
           ]
       })