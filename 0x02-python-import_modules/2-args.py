#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = len(sys.argv)

    if(args == 1):
        print("0 argumets.")
    elif(args == 2):
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(args - 1))
        for i in range(1, args):
            print("{}: {}".format(i, sys.argv[i]))
