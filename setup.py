from setuptools import setup, find_packages

from pyhive import (
    __license__ as license,
    __author__ as author,
    __title__ as title,
    __version__ as version
)

setup(
    name=title,
    version=version,
    packages=find_packages("pyhive"),
    url="https://github.com/WeebWare/PyHive",
    license=license,
    author=author,
    author_email="",
    description="Python API wrapper for the CoinHive HTTP API",
    long_description="Synchronous API wrapper for the CoinHive HTTP API",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License"
    ],
    keywords=[
        "coinhive"
    ],
    install_requires=[
        "requests"
    ]
)
