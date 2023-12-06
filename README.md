# Starter Template for Python Django projects

Use this cookiecutter template 🍪 to start every new Django Python project.

## System Dependencies

- Git
- Python 3.11
- [Poetry](https://python-poetry.org/docs/#installation) 1.2.x
- [Pre-commit hooks](https://pre-commit.com/)


## Getting Started

Create a new Python Django project

```
cookiecutter gh:papamana/cookiecutter-django
```

Create a new Python Django Project with Spesific Release version
```
cookiecutter git@github.com:papamana/cookiecutter-django.git --checkout <release version>
```
example:
```
cookiecutter git@github.com:papamana/cookiecutter-django.git --checkout v0.1-beta.1
```

For Windows, you might need to run `python -m cookiecutter` as the command might not work even though it's correctly configured on the PATH.


## What's inside

The template covers your back with the following elements:

- README.md with a pre-defined structure.
- CHANGELOG.md file with an initial message.
- Stub project template.
- Test directory with a sample test file.
- GitHub workflow configuration to run pytest automatically.
- Pre-configured mypy, Flake8, isort.
- A set of pre-commit hooks.
- pyproject.toml for Poetry.



## How to use it

Before creating a project:

- Install [Poetry](https://python-poetry.org/docs/#installation).
- Install [pre-commit](https://pre-commit.com/).
- Choose a project name. Likely, in the format `foo-bar` and create a GitHub
  repository for it. The root package of your project will have a default
  name `foo_bar`. Make sure that you made the repository private if you plan to create
  a private (non-open-source) project.
- Choose the license. For public projects, use MIT. For private projects, use "Proprietary."

The project generation runs these steps:

- Creates a new project from the template.
- Initializes a GitHub repository.
- Installs pre-commit hooks and updates all hooks to their latest versions.
- Create an initial commit.

After creating a project:

- Initialize the virtual environment and install all dependencies with `poetry install`.
- Deploy changes to GitHub.
- For Windows, you might need to change your access token to GitHub. See information [here](https://github.com/gitextensions/gitextensions/issues/4916#issuecomment-557509451)

Other hints:

- Use [How to Write Good Documentation](https://www.sohamkamani.com/blog/how-to-write-good-documentation/)
  to fill in our README with the content.
- Use [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) guideline for your
  changelog entries.

## Tests with GitHub actions

A file `.github/workflows/tests.yml` is responsible for running tests on GitHub.

## How to configure VSCode

At the moment, VSCode doesn't automatically detect Poetry environments. You can set it
manually, though. For a newly created project, create a `.vscode/settings.json`

```
poetry install
mkdir -p .vscode
cat <<EOF > .vscode/settings.json
{
  "python.pythonPath": "$(poetry env info -p)/bin/python"
}
EOF
```

Ref: https://github.com/microsoft/vscode-python/issues/8372

## Using .env with VSCode

If you use VSCode and the [vscode-dotenv](https://github.com/mikestead/vscode-dotenv)
extension, add the following lines to your `.vscode/settings.json` file:

```json
"files.associations": {
  "env.example": "dotenv",
  "env.github-actions": "dotenv"
}
```

## How to contribute

- If you have questions, ideas or suggestions, write them down in an issue.
- If you have a fix or an enhancement, create a pull request.

## ORIGIN PROJECT
- fork from [Cookiecutter Python Project](https://github.com/imankulov/cookiecutter-python-project)
