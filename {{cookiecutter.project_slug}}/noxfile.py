import nox
import os

PROJECT_ROOT = os.path.abspath(os.getcwd())


@nox.session(python=["3.6", "3.7", "3.8"])
def test(session):
    """
    Runs the test suite against all supported python versions.
    """
    session.install("-r", "requirements_dev.txt")
    # Posargs allows passing of tests directly
    tests = session.posargs or ["tests/"]
    session.run("pytest", *tests)


@nox.session
def lint(session):
    """
    Runs flake8 linting.
    """
    session.install("-r", "requirements_dev.txt")
    session.run("flake8", "{{cookiecutter.project_slug}}")


@nox.session
def format(session):
    """
    Formats project with black and isort (import order formatting).
    """
    session.install("-r", "requirements_dev.txt")
    session.run("black", "{{cookiecutter.project_slug}}")
    session.run("isort", "--recursive", "-y", "{{cookiecutter.project_slug}}")


@nox.session
def docs(session):
    """
    Builds project docs with sphinx.
    """
    build_dir = os.path.join(PROJECT_ROOT, "docs", "build")
    source_dir = os.path.join(PROJECT_ROOT, "docs", "source")

    # Clean any pre-built docs first
    session.run("rm", "-rf", build_dir, external=True)
    session.install("-r", "requirements_dev.txt")
    session.install(".")
    session.cd("docs")

    sphinx_args = ["-b", "html", source_dir, build_dir]

    # Checks if running locally or on travis
    # If local, auto serves docs on default browser
    if not session.interactive:
        sphinx_cmd = "sphinx-build"

    else:
        sphinx_cmd = "sphinx-autobuild"
        sphinx_args.insert(0, "--open-browser")

    session.run(sphinx_cmd, sphinx_args)
