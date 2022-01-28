#!/usr/bin/env python

import os
import sys

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

packages = ["responses"]

requires = [
    'charset_normalizer~=2.0.0; python_version >= "3"',
    'chardet>=3.0.2,<5; python_version < "3"',
    'idna>=2.5,<3; python_version < "3"',
    'idna>=2.5,<4; python_version >= "3"',
    'urllib3>=1.21.1,<1.27',
    'certifi>=2017.4.17'
]

test_requirements = [
    'pytest-httpbin==0.0.7',
    'pytest-cov',
    'pytest-mock',
    'pytest-xdist',
    'PySocks>=1.5.6, !=1.5.7',
    'pytest>=3'
]

about = {}

with open(os.path.join(here, 'responses', '__version__.py'), 'r', encoding='utf-8') as f:
    exec(f.read(), about)

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()


setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE']},
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=requires,
    license=about['__license__'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
    tests_require=test_requirements,
    extras_require={
        'security': [],
        'socks': ['PySocks>=1.5.6, !=1.5.7'],
        'use_chardet_on_py3': ['chardet>=3.0.2,<5']
    },
    project_urls={
        'Documentation': 'https://requests.readthedocs.io',
        'Source': 'https://github.com/psf/requests',
    },
)
