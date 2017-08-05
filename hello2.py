#!/usr/bin/env python3

"""This is a docstring."""
# import modules used here -- sys is a very usual one
import sys

# Gather our code in a main() function


def main():
    """Run the main program."""
    print "Hello there", sys.argv[1]
    # Command line arguments are sys.argv[1], sys.argv[2]
    # sys.argv[0] is the command itself and can be ignored


# Standard boilerplate to call main() function to begin
# the program


if __name__ == '__main__':
    main()
