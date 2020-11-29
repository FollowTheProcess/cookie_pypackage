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


@nox.session(python="3.9")
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


@nox.session(python="3.9")
def docs(session):
    """
    Build the documentation.
    """
    build_dir = str(PROJECT_ROOT.joinpath("docs/_build/html"))
    source_dir = str(PROJECT_ROOT.joinpath("docs/"))
    sphinx_args = ["-b", "html", source_dir, build_dir]

    # Clean any pre-built docs
    session.run("rm", "-rf", build_dir, external=True)
    session.install(
        "sphinx",
        "sphinx-autobuild",
        "sphinx-rtd-theme",
        "recommonmark",
    )
    session.install(".")
    session.run("sphinx-build", *sphinx_args)
