#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    long = len(sys.argv)
    res = 0
    for i in range(1, long):
        res = int(sys.argv[i]) + res
    print(res)
