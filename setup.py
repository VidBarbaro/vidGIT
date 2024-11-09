# setuptools - collection of utilities for packaging py projects
from setuptools import setup

# package setup
setup (name = 'vidGIT',
       version = '1.0',
       packages = ['vidGIT'],
       entry_points = {
           'console_scripts' : [ # command line scripts
               'vidGIT = vidGIT.cli:main' # command vidGIT calls the main func from the cli.py module
           ]
       })