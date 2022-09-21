#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print(i);
    else:
        print('{}'.format(str(i).rjust(2, '0')), end=', ')
