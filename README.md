# Cookie Pypackage

![License](https://img.shields.io/github/license/FollowTheProcess/cookie_pypackage.svg)
[![PyUp](https://pyup.io/repos/github/FollowTheProcess/cookie_pypackage/shield.svg)](https://pyup.io/repos/github/FollowTheProcess/cookie_pypackage/)

My take on the cookiecutter pypackage project template. Inspired by the [original](https://github.com/audreyr/cookiecutter-pypackage/) with some tweaks.

I created it from scratch, taking inspiration from other templates mostly as a learning exercise. However, feel free to use it!

## Changes from the Original

* Changed from tox to nox automated testing

* Pytest only

* Changed from sphinx to mkdocs

* Changed from readthedocs to github pages.

## Features

* [GitHub Actions](https://docs.github.com/en/free-pro-team@latest/actions): Ready for GitHub actions CI.

* [Nox](https://nox.thea.codes/en/stable/): Automated testing for python 3.6+

* [Invoke](http://www.pyinvoke.org): Easy project automation

* [Mkdocs](https://www.mkdocs.org): Easy markdown docs with Mkdocs, mkapi, and github pages

* [Versioneer](https://github.com/python-versioneer/python-versioneer): Pre-configured version bumping, all you need to do is create a new tag.

* [GitHub cli](https://cli.github.com): Option to use the new gh cli to create a GitHub repo for you after project creation. (You'll need to have this already set up)

* Auto-release to [PyPI](https://pypi.org) when you create a new release on GitHub and the tests pass.

## Usage

* Ensure you have cookiecutter installed:

``` shell
# Mac
brew install cookiecutter

# Linux
apt-get install cookiecutter

# Python
pip install --upgrade cookiecutter
```

* Navigate to where you keep your projects

* Call cookiecutter with this template and answer all the questions

``` shell
cookiecutter https://github.com/FollowTheProcess/cookie_pypackage.git
```

* Create a virtual environment, a git repo (if not using the gh cli) and start developing

``` shell
cd <name_of_your_project>

python3 -m venv venv

# Activate the venv and install dependencies
source venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
pip install -r requirements_dev.txt
```

* Install versioneer...

``` shell
versioneer install
```

* Make a first commit to set up the github repo (if not used the gh cli)

* Add repo to Pyupio

* Generate a GitHub [personal access token](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token). **KEEP THIS SAFE SOMEWHERE LOCAL, YOU ONLY GET TO SEE IT ONCE!**

* Add your token to the repository secrets and name it `PAGES_TOKEN`

* If you wish to deploy packages to PyPI using the `release` workflow, you will also need to add your PyPI username and password to the repository secrets as `PYPI_USERNAME` and `PYPI_PASSWORD` respectively.

* That should be it, from now on everything will be handled automatically. All you need to do is write code, tests and docs! Your code will be style checked, your tests will be run and your docs will be automatically deployed to GitHub Pages if the build is a success.
