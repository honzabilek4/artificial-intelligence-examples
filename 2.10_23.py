#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import LinkedList, Cons, Nil

def stree(graph):
    for edge in member_anyX(graph):
        for kostra in spread(LinkedList([edge]), graph):
            yield kostra

def spread(akumulator_kostry, graph):
    for akumulator_kostry1 in addedge(akumulator_kostry, graph):
        for kostra in spread(akumulator_kostry1, graph):
            yield kostra
    try:
        next(addedge(akumulator_kostry, graph))
    except StopIteration: # nelze pridat hranu
        yield akumulator_kostry

def addedge(akumulator_kostry, graph):
    for x, y in adjacent_anyXY(graph):
        if node(x, akumulator_kostry) and not node(y, akumulator_kostry):
            yield Cons((x, y), akumulator_kostry)

def adjacent_anyY(x, edges):
    for a, b in member_anyX(edges):
        if x == a:
            yield b
        if x == b:
            yield a

def adjacent_anyXY(edges):
    for a, b in member_anyX(edges):
        yield (a, b)
        yield (b, a)

def node(x, graph):
    try:
        next(adjacent_anyY(x, graph))
        return True
    except StopIteration:
        return False

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

# demonstracni vypis
if __name__ == "__main__":
    print('Kostra grafu')
    print('Volani stree(LinkedList([("a", "b"), ("b", "c"), ("b", "d"), ("c", "d")])) vrati:')
    for kostra_ in stree(LinkedList([("a", "b"), ("b", "c"), ("b", "d"), ("c", "d")])):
        print('  %s' % kostra_)
