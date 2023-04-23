# Python Project Template
Repository template for Python projects. The repository includes support for 
the following tools:
* pipenv
* setuptools
* pytest
* twine

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

## Running the tests

```sh
# Run the tests in the test directory
python -m pytest test
```

## Publishing the project
```sh
twine upload --repository python_template_project dist/*
```
