#! /usr/bin/env bash
if ["{{cookiecutter.use_gh_cli_to_create_repo}}" = "y"]; then
    gh repo create {{cookiecutter.github_username}}/{{cookiecutter.project_slug}}
fi
