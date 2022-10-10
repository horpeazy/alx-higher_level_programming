#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while i < x:
            print("{:d}".format(my_list[i]), end="" if i != x -1 else '\n')
            i += 1
    except Exception as e:
        print("")
    finally:
        return (i)