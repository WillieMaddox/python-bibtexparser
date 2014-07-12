#!/usr/bin/env python

from setuptools import setup
from bibtexparser import info

setup(
    name         = 'bibtexparser',
    version      = info.VERSION,
    url          = info.URL,
    author       = "Francois Boulogne",
    license      = info.LICENSE,
    author_email = info.EMAIL,
    description  = info.SHORT_DESCRIPTION,
    packages     = ['bibtexparser'],
    test_suite   = "bibtexparser.tests",
)
