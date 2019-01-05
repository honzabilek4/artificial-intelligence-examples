#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import LinkedList, Nil

def minimax(pos):
    poslist = moves(pos)
    if poslist == Nil:
        return (None, staticval(pos))
    return best(poslist)

def best(poslist):
    pos1 = poslist.head
    if poslist.tail == Nil:
        return minimax(pos1)
    _, val1 = minimax(pos1)
    pos2, val2 = best(poslist.tail)
    return better_of(pos1, val1, pos2, val2)

def better_of(pos0, val0, pos1, val1):
    if min_to_move(pos0) and val0 > val1 or max_to_move(pos0) and val0 < val1:
        return (pos0, val0)
    return (pos1, val1)

start = "root"
graph = dict(
    root=("max", LinkedList(["a1", "a2", "a3"])),
    a1=("min", LinkedList(["b1", "b2", "b3"])),
    a2=("min", LinkedList(["c1", "c2", "c3"])),
    a3=("min", LinkedList(["d1", "d2", "d3"])),
    b1=("max", Nil), b2=("max", Nil), b3=("max", Nil),
    c1=("max", Nil), c2=("max", Nil), c3=("max", Nil),
    d1=("max", Nil), d2=("max", Nil), d3=("max", Nil))

def moves(pos):
    # zavisi na resenem problemu
    return graph[pos][1]

def min_to_move(pos):
    return graph[pos][0] == "min"

def max_to_move(pos):
    return graph[pos][0] == "max"

staticvals = dict(
    b1=3, b2=12, b3=8,
    c1=2, c2=4, c3=6,
    d1=14, d2=5, d3=2)

def staticval(pos):
    # zavisi na resenem problemu
    if pos not in staticvals:
        raise ValueError("Uzel %s neni cilovy." % pos)
    return staticvals[pos]

# demonstracni vypis
if __name__ == "__main__":
    print("Minimax - hra na jedno kolo\n")

    print("            root            ")
    print("      a1     a2     a3      ")
    print("b1 b2 b3  c1 c2 c3  d1 d2 d3\n")

    print(" 3 12  8   2  4  6  14  5  2\n")

    print("Vysledek volani minimax('root'): %s" % (minimax("root"),))
