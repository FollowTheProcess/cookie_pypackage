from pathlib import Path

import nox

PROJECT_ROOT = Path(__file__).parent.resolve()


@nox.session(python=["3.7", "3.8", "3.9"])
def test(session):
    """
    Runs the test suite against all supported python versions.
    """
    session.install("-r", "requirements_dev.txt")
    session.install(".")
    # Posargs allows passing of tests directly
    tests = session.posargs or ["tests/"]
    session.run("pytest", *tests)


@nox.session()
def style(session):
    """
    Formats project with black and isort, then runs flake8 and mypy linting.
    """
    files = [
        "{{cookiecutter.project_slug}}",
        "tests",
        "noxfile.py",
        "tasks.py",
        "setup.py",
    ]

    session.install("-r", "requirements_dev.txt")
    session.run("black", *files)
    session.run("isort", *files)
    session.run("flake8", *files)
    session.run("mypy", *files)


@nox.session()
def docs(session):
    """
    Builds project docs with mkdocs.
    """
    # Clean any pre-built docs first
    session.install("-r", "requirements_dev.txt")
    session.install(".")

    # Checks if running locally or on travis
    # If local, auto serves docs on default browser
    if not session.interactive:
        session.run("mkdocs", "build", "--clean")

    else:
        session.run("mkdocs", "build", "--clean")
        session.run("mkdocs", "serve")
