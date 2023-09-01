from typing import List

def print_hello_to(subject: str) -> None:
    print("hello {0}".format(subject))

def concatenate_strings(strings: List[str]) -> str:
    concatenated = ""
    for string in strings:
        concatenated += string
    return concatenated
