#! /usr/bin/env bash

# If GitHub cli used to create remote repo
# This script will create the local repo, link the two together, and make an initial commit

{% if cookiecutter.use_gh_cli_to_create_repo == 'y' -%}

cd {{cookiecutter.project_slug}}

git init
git add -A
git commit -m "Initial Commit (Automated at Project Creation)"
git remote add origin git@github.com:{{cookiecutter.author_github_username}}/{{cookiecutter.project_slug}}.git
git branch -M main
git push --set-upstream origin main

{% endif %}