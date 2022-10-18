#!/usr/bin/python3

class LockedClass(object):
    def __setattr__(self, __name: str, __value) -> None:
        if __name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute 'last_name'")
        object.__setattr__(self, __name, __value)