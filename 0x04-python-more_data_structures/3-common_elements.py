#!/usr/bin/python3

def common_elements(set_1, set_2):
    list_ = []
    for elem in set_1:
        for elem_ in set_2:
            if elem == elem_:
                list_.append(elem)

    return set(list_)
