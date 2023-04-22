# python_template
Repository template for Python projects.

## Virtual Environment

```sh
# Install pipenv
pip3 install --user pipenv
```

```sh
# Install dependencies and setup environment
pipenv install --dev

# Activate the environment
pipenv shell
```

## Building

```sh
python setup.py bdist_wheel sdist
```

## Testing

```sh
# Run the tests in the test directory
python -m pytest test
```

## Publishing
```sh
twine upload --repository python_template_project dist/*
```
