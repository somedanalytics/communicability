#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pip.req import parse_requirements
from setuptools import setup

__version__ = "0.1"
__author__ = "Orcun Gumus <gumus@somed.io>"

long_description = open('README.rst').read()

install_reqs = parse_requirements("requirements.txt", session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='communicability',
    version=__version__,
    description='A package for help communicability calculation',
    long_description=long_description,
    author=__author__,
    author_email='orcungumus@gmail.com',
    install_requires=reqs,
    url='https://github.com/somedanalytics/communicability',  # use the URL to the github repo
    download_url='https://github.com/guemues/communicability/archive/1.0.tar.gz'
)