# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at <{{cookiecutter.project_github_url}}/issues>.

If you are reporting a bug, please use the issue template.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Write Docs

{{cookiecutter.project_name}} could always use more documentation, whether as part of the official docs, in docstrings, or even on the web in blog posts, articles etc.

### Submit Feedback

The best way to send feedback is to file an issue at <{{cookiecutter.project_github_url}}/issues>.

If you are proposing a feature:

* Explain in detail how it would work.

* Keep the scope as narrow as possible, to make it easier to implement.

* Remember that this is a volunteer driven project and contributions are welcome!

## Get Started

Ready to contribute? Here's how to set up `{{cookiecutter.project_slug}}` for local development.

1) Fork the `{{cookiecutter.project_slug}}` repo on GitHub.

2) Clone your fork locally:

``` shell
git clone https://github.com/<your_username>/{{cookiecutter.project_slug}}.git
```

3) Install your local copy, along with the development dependencies, into a virtualenv (note the dot telling pip to install from project directory):

``` shell
# Navigate to where your local clone is
cd {{cookiecutter.project_slug}}

# Create a virtualenv, called whatever you like, and activate it (convention is 'venv')
python3 -m venv <env_name>
source <env_name>/bin/activate

# Ensure build tools are updated
python3 -m pip install --upgrade pip setuptools wheel

# Install development dependencies
python3 -m pip install -r requirements_dev.txt

# Finally, install the project in editable mode
python3 -m pip install -e .

# Alternatively, the last two can be replaced by
python3 -m pip install -e .[dev]

# If using zsh not bash, you need to escape the square brackets
python3 -m pip install -e .\[dev\]
```

4) Create a branch for local development:

``` shell
git checkout -b <name_of_your_bugfix_or_feature>
```

Now you can make any changes locally.

5) When you're happy with your changes, run the local tests using nox. Nox makes this super easy, just run:

``` shell
nox
```

Nox will run a bunch of tests against different python versions (some of these will be skipped if you don't have a particular interpreter, don't worry this is normal! These will all be run automatically by Travis later). It will also format your code using black, run some linting, and check the docs build.

6) If the tests pass and you're happy, commit your changes and push your branch to GitHub:

``` shell
git add <file(s)_you_changed>
git commit

# Now write a nice descriptive commit message

git push origin <name_of_your_bugfix_or_feature>
```

7) Submit a pull request on GitHub

### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1) If you have implemented a new feature, make sure you have written tests for that feature

2) If you fixed a bug, make sure you have written tests that would have caught the bug you fixed

3) If the pull request adds functionality, the documentation should be updated

4) The pull request should work for all supported python versions. Check [https://travis-ci.com/{{cookiecutter.author_github_username}}/{{cookiecutter.project_slug}}/pull_requests](https://travis-ci.com/{{cookiecutter.author_github_username}}/{{cookiecutter.project_slug}}/pull_requests).

5) Do not delete your branch until your pull request has been reviewed, any requested changes have been made and it has been successfully merged and all tests passed

### Deploying

A reminder for maintainers on how to deploy. Make sure all your changes are committed (including an entry in changes.md). Then run:

``` shell
git tag x.x.x # Version number
git push --tags
```

Versioneer will take care of the rest.

Travis will then deploy to PyPI if tests pass.
