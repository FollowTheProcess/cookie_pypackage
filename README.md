# Cookie Pypackage

![License](https://img.shields.io/github/license/FollowTheProcess/cookie_pypackage.svg)
[![PyUp](https://pyup.io/repos/github/FollowTheProcess/cookie_pypackage/shield.svg)](https://pyup.io/repos/github/FollowTheProcess/cookie_pypackage/)

My take on the cookiecutter pypackage project template. Inspired by the [original](https://github.com/audreyr/cookiecutter-pypackage/) with some tweaks.

I created it from scratch, taking inspiration from other templates mostly as a learning exercise. However, feel free to use it!

## Changes from the Original

* Changed from tox to nox automated testing

* Pytest only

* Changed from sphinx to mkdocs

* Removed readthedocs in favour of github pages

## Features

* [Travis-CI](https://travis-ci.com): Ready for Travis CI testing.

* [Nox](https://nox.thea.codes/en/stable/): Automated testing for python 3.6+

* [Mkdocs](https://www.mkdocs.org): Easy markdown docs with Mkdocs and mkapi.

* [bump2version](https://github.com/c4urself/bump2version): Pre-configured version bumping with a single command

* Auto-release to [PyPI](https://pypi.org) when you push a new tag to master
