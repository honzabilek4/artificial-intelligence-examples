#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import LinkedList, Cons, Nil

def solution():
    for xs in sol(LinkedList(range(1, 9)), LinkedList(range(1, 9)),
                  LinkedList(range(-7, 8)), LinkedList(range(2, 17))):
        yield xs

def sol(dx, dy, du, dv):
    if dx == Nil:
        if dy == Nil:
            yield Nil # umistili jsme osm dam
        else:
            return # umistili jsme mene nez osm dam
    else:
        x = dx.head
        for y, dy1 in del_anyX(dy):
            for du1 in del_(du, x - y):
                for dv1 in del_(dv, x + y):
                    for others in sol(dx.tail, dy1, du1, dv1):
                        yield Cons(y, others)

def del_(xs, x):
    if xs == Nil:
        return
    if x == xs.head:
        yield xs.tail
    else:
        for ys in del_(xs.tail, x):
            yield Cons(xs.head, ys)

def del_anyX(xs):
    if xs == Nil:
        return
    yield xs.head, xs.tail
    for y, ys in del_anyX(xs.tail):
        yield y, Cons(xs.head, ys)

# demonstracni vypis
if __name__ == "__main__":
    print("PROBLEM OSMI DAM I")
    print("Volani next(solution()) : %s" % next(solution()))
