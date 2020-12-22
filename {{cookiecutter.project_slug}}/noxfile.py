"""
Nox configuration file for the project.
"""

from pathlib import Path

import nox

PROJECT_ROOT = Path(__file__).parent.resolve()

# Nox defaults to virtualenv which is now deprecated
nox.options.default_venv_backend = "venv"


@nox.session(python=["3.6", "3.7", "3.8", "3.9"])
def test(session):
    """
    Runs the test suite against all supported python versions.
    """
    session.install("--upgrade", "pip", "setuptools", "wheel")
    session.install(".")
    session.install("pytest", "pytest-cov")
    # Posargs allows passing of tests directly
    tests = session.posargs or ["tests/"]
    session.run("pytest", "--cov={{cookiecutter.project_slug}}", *tests)


@nox.session()
def coverage(session):
    """
    Test coverage analysis.
    """
    session.install("--upgrade", "pip", "setuptools", "wheel")
    session.install("coverage")

    session.run("coverage", "report", "--fail-under=96", "--show-missing")
    session.run("coverage", "erase")


@nox.session()
def lint(session):
    """
    Formats project with black and isort, then runs flake8 and mypy linting.
    """
    session.install("--upgrade", "pip", "setuptools", "wheel")
    session.install("black", "isort", "flake8", "mypy")
    session.run("isort", ".")
    session.run("black", ".")
    session.run("flake8", ".")
    session.run("mypy", ".")


@nox.session()
def docs(session):
    """
    Builds the project documentation.
    """
    session.install("--upgrade", "pip", "setuptools", "wheel")
    session.install(".")

    session.run("mkdocs", "build", "--clean")
