# Python Template Project

![Ubuntu](https://github.com/markvilar/python_project_template/actions/workflows/ubuntu.yml/badge.svg)
![Linter](https://github.com/markvilar/python_project_template/actions/workflows/pylint.yml/badge.svg)

This is a small template repository for creating python projects with a modern toolchain. 
The repository includes support for the following tools:
- poetry - package management and build system
- pytest - unit tests
- black - code linting


## Getting started

### Install poetry

```shell
# Install poetry
pip3 install --user poetry
```

### Configure the project environment

```shell
# Set the Python version
poetry env use <python_version>

# Validate the environment configuration
poetry env info
```

### Install dependencies and build the project

```shell
# Install dependencies
poetry install

# Build the project
poetry build

# Add new packages
poetry add <package-name>
```

### Running unit tests

```shell
poetry run pytest
```


## Other uses

### Managing the project environment

```shell
poetry env info
```

```shell
poetry env remove
```

### Activate the project environment in a shell

```shell
poetry shell
```

### Removing dependencies

```shell
poetry remove <package>
```
