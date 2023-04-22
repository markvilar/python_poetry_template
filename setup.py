from setuptools import find_packages, setup

with open("README.md", "r") as handle:
    long_description = handle.read()

setup(
    name="python_project_template",
    version = "0.0.1",
    description = "A template for Python projects with various development tools",
    package_dir = {"": "libtemp"},
    packages = find_packages(where="libtemp"),
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/markvilar/python_project_template",
    author = "markvilar",
    author_email = "martin.kvisvik.larsen@hotmail.com",
    license = "MIT",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires = ["bson >= 0.5.10"],
    extras_require = {
        "dev": ["pytest>=7.0"],
    },
    test_suite = "tests",
    python_requires = ">=3.10",
)
