#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import LinkedList, Cons, Nil
from best_search import BestSearch

biggest = 99
start = LinkedList([(2, 2), (3, 1), (2, 3), (2, 1), (3, 3), (1, 2), (3, 2), (1, 3), (1, 1)])
goal = LinkedList([(1, 3), (2, 3), (3, 3), (1, 2), (2, 2), (3, 2), (1, 1), (2, 1), (3, 1)])

def is_goal(state):
    return state == goal

def move_anyYC(numbers):
    if numbers == Nil:
        return
    xb, yb = numbers.head
    if xb > 1: # pohyb mezery doleva
        xl = xb - 1
        new_tail = replace((xl, yb), (xb, yb), numbers.tail)
        yield (Cons((xl, yb), new_tail), 1)
    if xb < 3: # pohyb mezery doprava
        xr = xb + 1
        new_tail = replace((xr, yb), (xb, yb), numbers.tail)
        yield (Cons((xr, yb), new_tail), 1)
    if yb > 1: # pohyb mezery dolu
        yd = yb - 1
        new_tail = replace((xb, yd), (xb, yb), numbers.tail)
        yield (Cons((xb, yd), new_tail), 1)
    if yb < 3: # pohyb mezery nahoru
        yu = yb + 1
        new_tail = replace((xb, yu), (xb, yb), numbers.tail)
        yield (Cons((xb, yu), new_tail), 1)

def replace(x, y, xs):
    if x == xs.head:
        return Cons(y, xs.tail)
    return Cons(xs.head, replace(x, y, xs.tail))

def h1(state):
    a, b, c, d, e, f, g, h, i = state
    return (a != (1, 3)) + (b != (2, 3)) + (c != (3, 3)) + \
           (d != (1, 2)) + (e != (2, 2)) + (f != (3, 2)) + \
           (g != (1, 1)) + (h != (2, 1)) + (i != (3, 1))

def h2(state):
    a, b, c, d, e, f, g, h, i = state
    return dist(a, (1, 3)) + dist(b, (2, 3)) + dist(c, (3, 3)) + \
           dist(d, (1, 2)) + dist(e, (2, 2)) + dist(f, (3, 2)) + \
           dist(g, (1, 1)) + dist(h, (2, 1)) + dist(i, (3, 1))

def dist(a, b): # manhattanska vzdalenost
    xa, ya = a
    xb, yb = b
    return abs(xa-xb) + abs(ya-yb)

def writelist(xs):
    writelist_(xs, 1)

def writelist_(xs, i):
    if xs != Nil:
        print("%d: %s" % (i, xs.head))
        writelist_(xs.tail, i+1)

def length(xs):
    if xs == Nil:
        return 0
    return 1 + length(xs.tail)

# demonstracni vypis
if __name__ == "__main__":
    print("8-posunovacka, algoritmus A*\n")
    print("Pocatecni stav: %s" % start)

    print("\nNalezene reseni (heuristika h1):")
    astar = BestSearch(biggest, is_goal, move_anyYC, h1)
    solution = next(astar.search(start))
    print("Prohledano %d stavu, vysledne reseni ma cenu %d." % (astar.total, length(solution)-1))
    writelist(solution.reverse())

    print("\nNalezene reseni (heuristika h2):")
    astar = BestSearch(biggest, is_goal, move_anyYC, h2)
    solution = next(astar.search(start))
    print("Prohledano %d stavu, vysledne reseni ma cenu %d." % (astar.total, length(solution)-1))
    writelist(solution.reverse())
