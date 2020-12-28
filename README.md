# Cookie Pypackage

![License](https://img.shields.io/github/license/FollowTheProcess/cookie_pypackage.svg)
[![PyUp](https://pyup.io/repos/github/FollowTheProcess/cookie_pypackage/shield.svg)](https://pyup.io/repos/github/FollowTheProcess/cookie_pypackage/)

My take on the cookiecutter pypackage project template. Inspired by the [original](https://github.com/audreyr/cookiecutter-pypackage/) with some tweaks.

I created it from scratch, taking inspiration from other templates mostly as a learning exercise. However, feel free to use it!

## Changes from the Original

* Changed from tox to nox automated testing

* Pytest only

* Change CI provider from Travis to GitHub actions

* Change docs from Sphinx to MkDocs

* Made compliant with PEP 517/518

## Features

* [GitHub Actions](https://docs.github.com/en/free-pro-team@latest/actions): Ready for GitHub actions CI.

* [Nox](https://nox.thea.codes/en/stable/): Easy automation & testing for python 3.6+

* [MkDocs](https://www.mkdocs.org/#building-the-site): Production ready docs with MkDocs and GitHub Pages.

* [Bump2Version](https://pypi.org/project/bump2version/): Pre-configured version bumping, all you need to do is run a command

* [GitHub cli](https://cli.github.com): Option to use the new gh cli to create a GitHub repo for you after project creation. (You'll need to have this already set up)

* Auto-release to [PyPI](https://pypi.org) when you push a new version and the tests pass.

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

# Activate the venv, install dependencies and project root
source venv/bin/activate
python3 -m pip install -e .[dev] # Tells pip to install all development dependencies too
```

* Make a first commit to set up the github repo (if not used the gh cli)

* Add repo to Pyupio

* If you wish to deploy packages to PyPI using the `CI` workflow. You will need to create a [PyPI API Token](https://pypi.org/help/#apitoken) and save it in your repository secrets under the name `PYPI_API_TOKEN`.

* That should be it, from now on everything will be handled automatically. All you need to do is write code, tests and docs! Your code will be style checked, your tests will be run etc.

* I've left the deploying of docs to github pages manual. The docs will be built automatically and error if anything is wrong but they probably don't need deploying every time. When you're ready to deploy the docs to GitHub pages just run...

``` shell
mkdocs gh-deploy
```

* To create a new version and release to PyPI...

``` shell
bump2version patch # Possible: patch, minor, major
git push
git push --tags
```

* Don't worry, your package will only be uploaded to PyPI if all other CI actions pass (testing, linting, building docs etc.)
