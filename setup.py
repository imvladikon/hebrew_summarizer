#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()


def read_requirements(reqs_path):
    with open(reqs_path, encoding='utf8') as f:
        reqs = [
            line.strip()
            for line in f
            if not line.strip().startswith('#') and not line.strip().startswith('--')
        ]
    return reqs


setup(
    name="hebrew_summarizer",
    version="0.0.1",
    description="Hebrew summarization pipeline",
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/IAHLT/hebrew_summarizer',
    author='Liat Nativ',
    author_email='liatnativ@gmail.com',
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
    ],
    packages=find_packages(exclude=['tests*', 'scripts', 'utils']),
    include_package_data=True,
    install_requires=read_requirements(HERE / 'requirements.txt'),
)
