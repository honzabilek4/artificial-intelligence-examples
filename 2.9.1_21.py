#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import LinkedList, Cons, Nil

def path(a, z, graph):
    for cesta in path1(a, LinkedList([z]), graph, 1):
        yield cesta

def path1(a, akumulator_cesty, graph, depth):
    if akumulator_cesty.head == a:
        yield akumulator_cesty
    else:
        y = akumulator_cesty.head
        for x in adjacent_anyX(y, graph):
            if not member(x, akumulator_cesty):
                for cesta in path1(a, Cons(x, akumulator_cesty), graph, depth+1):
                    yield cesta

def adjacent_anyX(y, graph):
    _, edges = graph
    for a, b in member_anyX(edges):
        if y == a:
            yield b
        if y == b:
            yield a

def member(x, xs):
    if xs == Nil:
        return False
    if x == xs.head:
        return True
    return member(x, xs.tail)

def member_anyX(xs):
    if xs == Nil:
        return
    yield xs.head
    for x in member_anyX(xs.tail):
        yield x

_graph = (LinkedList(["a", "b", "c", "d"]),
          LinkedList([("a", "b"), ("b", "d"), ("b", "c"), ("c", "d")]))

# demonstracni vypis
if __name__ == "__main__":
    print('Cesta v grafu\n')
    print('next(path("a", "c", _graph)) : %s' % next(path("a", "c", _graph)))
