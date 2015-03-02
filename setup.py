#!/usr/bin/env python
from distutils.core import setup, Command

from pyeuler import VERSION

with open('README.rst', 'rb') as fin:
    README = fin.read()

PACKAGE_NAME = 'pyeuler'

requires = [
    'requests',
    'docopt',
    'clint',
]

tests_require = [
    'pytest',
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description='Command line tool for checking Project Euler solutions',
      long_description=README,
      author='Ben Emery',
      url='https://github.com/benemery/%s' % PACKAGE_NAME,
      download_url='https://github.com/benemery/%s/tarball/%s' % (VERSION, PACKAGE_NAME),
      packages=[PACKAGE_NAME, ],
      install_requires=requires,
      entry_points={
        'console_scripts': [
          'py.euler = pyeuler:main',
        ]
      },
      extras_require={
        'tests': tests_require,
    },
)