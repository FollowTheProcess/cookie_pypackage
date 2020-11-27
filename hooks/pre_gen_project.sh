#! /usr/bin/env bash

# Use GitHub cli to create a remote repo

{% if cookiecutter.use_gh_cli_to_create_repo == 'y' -%}

gh repo create {{cookiecutter.author_github_username}}/{{cookiecutter.project_slug}}

{% endif %}
