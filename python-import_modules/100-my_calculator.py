#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    long = len(argv)
    if long != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        er1 = "Unknown operator. Available operators: +, -, * and /"
        if argv[2] == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif argv[2] == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif argv[2] == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif argv[2] == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("{}".format(er1))
            exit(1)
