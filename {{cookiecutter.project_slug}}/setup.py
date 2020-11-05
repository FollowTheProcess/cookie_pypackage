from pathlib import Path

from setuptools import find_packages, setup

ROOT = Path(__file__).parent.resolve()


def read(path: str, encoding: str = "utf-8") -> str:
    """
    Utility function to read the content of files to
    be passed to setup arguments.
    """

    root_path = ROOT.joinpath(path)
    with open(root_path, encoding=encoding) as fp:
        return fp.read()


def get_install_requirements(path: str) -> list:
    """
    Utility function to read a requirements.txt type file.
    """
    content = read(path)
    return [
        req for req in content.split("\n") if req != "" and not req.startswith("#")
    ]


setup(
    name="{{cookiecutter.project_slug}}",
    version="{{cookiecutter.project_version}}",
    description="{{cookiecutter.project_short_description}}",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="{{cookiecutter.project_github_url}}",
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    classifiers=[
        # Update this before release
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=["tests", "docs"]),
    python_requires=">=3.7",
    install_requires=get_install_requirements("requirements.txt"),
    extras_require={"dev": get_install_requirements("requirements_dev.txt")},
    license="{{cookiecutter.open_source_license}}",
    test_suite="tests",
    zip_safe=False,
)
