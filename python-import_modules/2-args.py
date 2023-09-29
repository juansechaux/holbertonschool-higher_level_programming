#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    long = len(sys.argv) - 1
    if long == 0:
        print("{} arguments.".format(long))
    elif long == 1:
        print("{} argument:".format(long))
        print("{}: {}".format(long, sys.argv[1]))
    else:
        print("{} arguments:".format(long))
        i = 1
        while i <= long:
            print("{}: {}".format(i, sys.argv[i]))
            i = i + 1
