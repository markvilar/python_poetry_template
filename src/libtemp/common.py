""" Module for common functions. """

def print_hello_to(subject: str) -> None:
    """ Prints hello to a subject. """
    print(f"hello {subject}")

def concatenate_strings(strings: list[str]) -> str:
    """ Concatenates a list of strings into a string. """
    return "".join(strings)
