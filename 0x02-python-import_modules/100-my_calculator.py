#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys


    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] not in ("+", "-", "*", "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif sys.argv[2] == "+":
        print(f"{a} + {b} = {add(a, b)}")
    elif sys.argv[2] == "-":
        print(f"{a} - {b} = {sub(a, b)}")
    elif sys.argv[2] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif sys.argv[2] == "/":
        print(f"{a} / {b} = {div(a, b)}")
