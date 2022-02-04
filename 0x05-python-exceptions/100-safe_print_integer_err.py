#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except TypeError as te:
        print("Exception:", te, file=sys.stderr)
    except ValueError as ve:
        print("Exception:", ve, file=sys.stderr)
    else:
        return(True)
