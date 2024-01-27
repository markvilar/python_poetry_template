""" 
Setup file for the template library package.
"""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="UTF-8") as handle:
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
    license = "GPLv3+",
    classifiers = [
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        "bson >= 0.5.10"
        "icecream >= 2.0.0"
        "loguru >= 0.7.0"
        "result"
        "tqdm >= 4.0.0"
    ],
    extras_require = {
        "dev": ["pytest>=7.0"],
    },
    test_suite = "tests",
    python_requires = ">=3.10",
)
