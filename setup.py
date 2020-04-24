#!/usr/bin/env python
import os
from setuptools import setup, find_packages


# https://packaging.python.org/guides/single-sourcing-package-version/
version = {}
with open(os.path.join("src", "undersample", "__init__.py")) as fp:
    exec(fp.read(), version)


# http://blog.ionelmc.ro/2014/05/25/python-packaging/
setup(
    name="undersample",
    version=version["__version__"],
    description="Python package for Undersampling Numpy Arrays using different techniques",
    author="Shreyas Bapat",
    author_email="hello@shreyasb.com",
    url="http://shreyasb.com/",
    download_url="https://github.com/shreyasbapat/undersample",
    license="MIT",
    keywords=["mri", "undersamplings"],
    python_requires=">=3.6",
    install_requires=["numpy",],
    extras_require={
        "dev": [
            "coverage",
            "pytest-cov",
            "pycodestyle",
            "sphinx",
            "sphinx_rtd_theme",
            "nbsphinx",
            "ipython>=5.0",
            "jupyter-client",
            "ipykernel",
            "ipywidgets",
        ]
    },
    packages=find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    long_description=open("README.rst", encoding="utf-8").read(),
    include_package_data=True,
    zip_safe=False,
)
