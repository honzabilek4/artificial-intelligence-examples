#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import LinkedList, Cons, Nil

def path(a, z, graph):
    for cesta, cena in path1(a, LinkedList([z]), 0, graph, 1):
        yield (cesta, cena)

def path1(a, akumulator_cesty, akumulator_ceny, graph, depth):
    if akumulator_cesty.head == a:
        yield (akumulator_cesty, akumulator_ceny)
    else:
        y = akumulator_cesty.head
        for x, cenaXY in adjacent_anyXcenaXY(y, graph):
            if not member(x, akumulator_cesty):
                for cesta, cena in path1(a, Cons(x, akumulator_cesty),
                                         akumulator_ceny + cenaXY, graph, depth+1):
                    yield (cesta, cena)

def adjacent_anyXcenaXY(y, edges):
    for a, b, cenaAB in member_anyX(edges):
        if y == a:
            yield (b, cenaAB)
        if y == b:
            yield (a, cenaAB)

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
    print('Cesta v grafu\n')
    cesta_, cena_ = next(path("s", "u", LinkedList([
        ("s", "t", 3), ("t", "v", 1), ("t", "u", 5), ("u", "t", 2), ("v", "u", 2)])))
    print('Cesta=%s' % cesta_)
    print('Cena=%d\n' % cena_)
