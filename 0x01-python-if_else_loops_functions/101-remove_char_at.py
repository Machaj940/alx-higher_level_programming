#!/usr/bin/python3
def remove_char_at(str, n):
    a = str[ :n]
    b = str[n + 1: ]
    return(a + b)
