#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as se:
        print("Exception:", se, file=sys.stderr)
        return(None)
    else:
        return(result)
