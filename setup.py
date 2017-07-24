#!/usr/bin/env python

from __future__ import unicode_literals
from setuptools import setup, find_packages
import io
import os

here = os.path.abspath(os.path.dirname(__file__))
README = io.open(os.path.join(here, 'README.rst'), encoding="utf8").read()

version = '0.5.0'
author = 'Netquity'
description = "Django-environ-docker allows you to utilize 12factor inspired " \
              "environment variables to configure your Django application with " \
              "Docker Secrets."
install_requires = ['django', 'six']

setup(name='django-environ-docker',
      version=version,
      description=description,
      long_description=README,
      classifiers=[
          # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Information Technology',
          'Framework :: Django',
          'Framework :: Django :: 1.8',
          'Framework :: Django :: 1.9',
          'Framework :: Django :: 1.10',
          'Framework :: Django :: 1.11',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
          'License :: OSI Approved :: MIT License',
          'Framework :: Django'
      ],
      keywords='django environment variables 12factor docker secrets',
      author=author,
      author_email='hello@netquity.com',
      url='https://github.com/netquity/django-environ',
      download_url='https://github.com/netquity/django-environ/archive/0.5.0.tar.gz',
      license='MIT License',
      packages=find_packages(),
      platforms=["any"],
      include_package_data=True,
      test_suite='environ.test.load_suite',
      zip_safe=False,
      install_requires=install_requires,
      )
