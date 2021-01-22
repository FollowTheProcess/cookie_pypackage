"""
Nox configuration file for the project.
"""

from pathlib import Path

import nox

PROJECT_ROOT = Path(__file__).parent.resolve()


@nox.session(python=["3.7", "3.8", "3.9"])
def test(session):
    """
    Runs the test suite against all supported python versions.
    """
    session.install("--upgrade", "pip", "setuptools", "wheel")
    session.install(".[test]")
    # Posargs allows passing of tests directly
    tests = session.posargs or ["tests/"]
    session.run("pytest", "--cov={{cookiecutter.project_slug}}", *tests)


@nox.session()
def coverage(session):
    """
    Test coverage analysis.
    """
    img_path = PROJECT_ROOT.joinpath("docs/img/coverage.svg")

    if not img_path.exists():
        img_path.parent.mkdir(parents=True)
        img_path.touch()

    session.install("--upgrade", "pip", "setuptools", "wheel")
    session.install(".[cov]")

    session.run("coverage", "report", "--show-missing")
    session.run("coverage-badge", "-fo", f"{str(img_path)}")
    session.run("coverage", "erase")


@nox.session()
def lint(session):
    """
    Formats project with black and isort, then runs flake8 and mypy linting.
    """
    session.install("--upgrade", "pip", "setuptools", "wheel")
    session.install(".[lint]")
    session.run("isort", ".")
    session.run("black", ".")
    session.run("flake8", ".")
    session.run("mypy", ".")


@nox.session()
def docs(session):
    """
    Builds the project documentation.

    You can also serve the docs by running:

    nox -s docs -- serve
    """
    session.install("--upgrade", "pip", "setuptools", "wheel")
    session.install(".[docs]")

    if "serve" in session.posargs:
        session.run("mkdocs", "serve")
    else:
        session.run("mkdocs", "build", "--clean")
