#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    long = len(argv)
    if long != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit (1)
    else:
        if argv[2] == "+":
            print("{} + {} = {}".format(argv[1], argv[3], add(argv[1], argv[3])))
        elif argv[2] == "-":
            print("{} - {} = {}".format(argv[1], argv[3], sub(argv[1], argv[3])))
        elif argv[2] == "*":
            print("{} * {} = {}".format(argv[1], argv[3], mul(argv[1], argv[3])))
        elif argv[2] == "/":
            print("{} / {} = {}".format(argv[1], argv[3], div(argv[1], argv[3])))
        else:
            print("{}".format("Unknown operator. Available operators: +, -, * and /"))
            exit (1)
