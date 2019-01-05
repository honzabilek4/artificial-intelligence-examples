#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

"""Lisp-like linked list data structure"""

Nil = []

class Cons(object):
    def __init__(self, x, xs):
        self.head = x
        self.tail = xs

    def reverse(self):
        result = Nil
        for x in self:
            result = Cons(x, result)
        return result

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.head == other.head and self.tail == other.tail
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.head < other.head or self.tail < other.tail

    def __gt__(self, other):
        return self.head > other.head or self.tail > other.tail

    def __iter__(self):
        return _Iterator(self)

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return str(self)

class _Iterator(object):
    def __init__(self, linked_list):
        self._linked_list = linked_list

    def __iter__(self):
        return self

    def next(self):
        if self._linked_list == Nil:
            raise StopIteration
        else:
            head = self._linked_list.head
            self._linked_list = self._linked_list.tail
            return head

    __next__ = next

def LinkedList(lst):
    result = Nil
    for x in reversed(lst):
        result = Cons(x, result)
    return result
