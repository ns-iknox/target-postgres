#!/usr/bin/env python

import shutil
from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

PSYCOPG2 = "psycopg2==2.8.5" if shutil.which("pg_config") else "psycopg2-binary==2.8.5"

setup(
    name="singer-target-postgres",
    url="https://github.com/datamill-co/target-postgres",
    author="datamill",
    version="0.2.4",
    description="Singer.io target for loading data into postgres",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["target_postgres"],
    python_requires="~=3.3",
    install_requires=[
        "arrow==0.15.5",
        PSYCOPG2,
        "singer-python==5.9.0"
    ],
    setup_requires=[
        "pytest-runner"
    ],
    extras_require={
        "tests": [
            "chance==0.110",
            "Faker==4.0.3",
            "pytest==5.4.1"
        ]},
    entry_points="""
      [console_scripts]
      target-postgres=target_postgres:cli
    """,
    packages=find_packages()
)
