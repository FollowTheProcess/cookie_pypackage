"""
Invoke tasks for project automation.

Run invoke --list to see options in command line.

Author: {{cookiecutter.author_name}}
"""
from invoke import task
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.resolve()


@task
def clean(c):
    """
    Recursively removes cache files and other clutter from the project.
    """
    c.run('find . -name "__pycache__" -exec rm -rf {} +')
    c.run('find . -name ".pytest_cache" -exec rm -rf {} +')
    c.run('find . -name ".ipynb_checkpoints" -exec rm -rf {} +')
    c.run('find . -name ".nox" -exec rm -rf {} +')


@task
def style(c):
    """
    Runs style checking and linting tools on the project.
    """
    c.run("isort .")
    c.run("flake8")
    c.run("black .")


@task
def test(c):
    """
    Runs the test suite.
    """
    c.run("pytest")


@task
def docs(c):
    """
    Builds mkdocs docs.
    """
    c.run("mkdocs build --clean")
    c.run("mkdocs serve")
