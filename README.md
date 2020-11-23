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

* [Nox](https://nox.thea.codes/en/stable/): Automated testing for python 3.7+

* [Invoke](http://www.pyinvoke.org): Easy project automation

* [Mkdocs](https://www.mkdocs.org): Easy markdown docs with Mkdocs, mkapi, and github pages

* [Versioneer](https://github.com/python-versioneer/python-versioneer): Pre-configured version bumping, all you need to do is create a new tag.

* Auto-release to [PyPI](https://pypi.org) when you push a new tag to master

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

* Create a virtual environment, a git repo and start developing

``` shell
cd <name_of_your_project>

python3 -m venv venv

# Activate the venv
source venv/bin/activate
```

* Make a first commit to set up the github repo

* Add repo to Pyupio

* Merge pyup config pull request

* Pull down changes

* Encrypt PyPI password with travis (nothing will be deployed unless you push a new git tag to main)

``` shell
travis encrypt --add deploy.password

# Will prompt to add PyPI password then press enter, then ctrl D
```

* Make a commit and push this encrypt

* Generate a GitHub [personal access token](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token). **KEEP THIS SAFE SOMEWHERE LOCAL, YOU ONLY GET TO SEE IT ONCE!**

* Add the repo to your Travis account and create an environment variable called `GITHUB_TOKEN` with the value of your GitHub personal access token.

* That should be it, from now on everything will be handled automatically. All you need to do is write code, tests and docs! Your code will be style checked, your tests will be run and your docs will be automatically deployed to GitHub Pages if the build is a success.
