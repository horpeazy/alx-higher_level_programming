#!/usr/bin/python3

for i in range(26):
    if i % 2 == 0:
        char = chr(ord('z') - i)
    else:
        char = chr(ord('Z') - i)
    print('{}'.format(char), end='')
