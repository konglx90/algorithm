# -*- coding: utf-8 -*-


class Stack(object):
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[len(self.item) - 1]

    def size(self):
        return len(self.item)
