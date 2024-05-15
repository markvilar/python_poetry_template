"""Module for the package entrypoint."""

from .common import print_hello_to

def main():
    """Main function for the entrypoint."""
    print_hello_to("world!")

if __name__ == "__main__":
    main()
