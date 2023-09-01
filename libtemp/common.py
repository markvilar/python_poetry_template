""" Module for common functions. """

from typing import List

def print_hello_to(subject: str) -> None:
    """ Prints hello to a subject. """
    print(f"hello {subject}")

def concatenate_strings(strings: List[str]) -> str:
    """ Concatenates a list of strings into a string. """
    return "".join(strings)
