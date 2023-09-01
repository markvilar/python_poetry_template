# Python Project Template

![ci](https://github.com/markvilar/python_project_template/actions/workflows/ci.yml/badge.svg)
![pylint](https://github.com/markvilar/python_project_template/actions/workflows/pylint.yml/badge.svg)

Repository template for Python projects. The repository includes support for 
the following tools:
* pipenv - management of virtual environments and dependencies
* setuptools - management of package setup
* pytest - unit tests
* twine - remote repository interaction

## Setting up a virtual environment

### Install pipenv

```sh
# Install pipenv
pip3 install --user pipenv
```

### Install dependencies and activate shell

```sh
# Install dependencies and setup environment
pipenv install --dev

# Activate an interactive shell for the virtual environment
pipenv shell
```

## Executing pipenv scripts

```sh
pipenv run tests
pipenv run main
pipenv run build
```

## Building binaries and sources

```sh
python setup.py bdist_wheel sdist
```

## Running tests

```sh
# Run specific tests
python -m unittest tests/test_common.py
python -m unittest tests/test_math.py

# Run specific tests in verbose mode
python -m unittest -v tests/test_common.py
python -m unittest -v tests/test_math.py
```

## Publishing the project
```sh
twine upload --repository python_template_project dist/*
```
