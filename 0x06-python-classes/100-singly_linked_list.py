#!/usr/bin/python3
"""
    This file contains class definitions of a node
    and a  singly linked list
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
            return
        node = self.__head
        prev = None
        while (node and node.data < value):
            prev = node
            node = node.next_node
        if node == self.__head:
            new_node = Node(value)
            new_node.next_node = self.__head
            self.__head = new_node
            return
        new_node = Node(value)
        new_node.next_node = node
        prev.next_node = new_node
        return

    def __str__(self):
        node = self.__head
        _str = ""
        while (node):
            _str += str(node.data)
            if node.next_node is not None:
                _str += "\n"
            node = node.next_node
        return _str
