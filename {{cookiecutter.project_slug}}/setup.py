#!/usr/bin/env python

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Read in README for long description
with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()

# Specify minimum requirements to run here
requirements = []

# Specify setup requirements here
setup_requirements = []

# Specify test requirements here
test_requirements = []

setup(
    name="{{cookiecutter.project_slug}}",
    version="{{cookiecutter.project_version}}",
    description="{{cookiecutter.project_short_description}}",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="{{cookiecutter.project_github_url}}",
    author_email="{{cookiecutter.author_email}}",
    classifiers=[
        # Update this before release
        "Development Status :: 2 - Pre-Alpha",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(),
    python_requires=">=3.6, <4",
    install_requires=requirements,
    license="{{cookiecutter.open_source_license}}",
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    zip_safe=False,
)
