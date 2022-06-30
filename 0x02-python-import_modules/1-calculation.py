#!/usr/bin/python3
# 1-calculation.py

if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 20 and 10."""
    from calculator_1 import add, sub, mul, div

    a = 20
    b = 10

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
