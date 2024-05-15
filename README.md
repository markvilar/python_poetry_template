# Benthoscan

![ci](https://github.com/markvilar/benthoscan/actions/workflows/ci.yml/badge.svg)
![pylint](https://github.com/markvilar/benthoscan/actions/workflows/pylint.yml/badge.svg)

Benthoscan is a small API for 3D reconstruction and registration based on images. Benthoscan wraps 
Metashapes Python API for reconstruction and implements a registration module with Open3D.

The repository includes support for the following tools:
* poetry - package management and build system
* pytest - unit tests


## Getting started

### Install poetry

```shell
# Install poetry
pip3 install --user poetry
```

### Configure the project environment

```shell
# Set the Python version to 3.11
poetry env use 3.11

# Validate the environment configuration
poetry env info
```

### Install dependencies and build the project

```shell
# Install dependencies
poetry install

# Build the project
poetry build
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
