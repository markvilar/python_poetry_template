# Python Project Template
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

# Activate the environment
pipenv shell
```

## Building binaries and sources

```sh
python setup.py bdist_wheel sdist
```

## Running tests

```sh
# Run specific tests
python -m unittest tests/math_tests.py

# Run specific tests in verbose mode
python -m unittest -v tests/math_tests.py
```

## Publishing the project
```sh
twine upload --repository python_template_project dist/*
```
