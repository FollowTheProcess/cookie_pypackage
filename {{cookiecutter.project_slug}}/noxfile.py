from pathlib import Path

import nox

PROJECT_ROOT = Path(__file__).parent.resolve()


@nox.session(python=["3.6", "3.7", "3.8", "3.9"])
def test(session):
    """
    Runs the test suite against all supported python versions.
    """
    session.install(".")
    session.install("pytest", "pytest-cov")
    # Posargs allows passing of tests directly
    tests = session.posargs or ["tests/"]
    session.run("pytest", "--cov={{cookiecutter.project_slug}}", *tests)


@nox.session()
def style(session):
    """
    Formats project with black and isort, then runs flake8 and mypy linting.
    """

    session.install("black", "isort", "flake8", "mypy")
    session.install(".")
    session.run("isort", ".")
    session.run("black", ".")
    session.run("flake8", ".")
    session.run("mypy", ".")


@nox.session()
def docs(session):
    """
    Builds project docs with mkdocs.
    """
    # Clean any pre-built docs first
    session.install("mkdocs", "mkapi")
    session.install(".")

    session.run("mkdocs", "build", "--clean")
