#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import LinkedList, Cons, Nil
from and_or_best_search import BestSearch

biggest = 99
start = ("direct", "a", "z")

stateS = dict(a=True, b=True, c=True, d=True, e=True)
stateU = dict(u=True, v=True, x=True, y=True, z=True)
borders = dict(l=True, k=True)
distances = dict(
    a=[("b", 2), ("c", 3)],
    b=[("d", 2)],
    c=[("e", 1), ("l", 2)],
    d=[("k", 1)],
    e=[("k", 3), ("l", 2)],
    k=[("u", 2), ("x", 3)],
    l=[("u", 1)],
    u=[("v", 5), ("y", 2)],
    x=[("y", 3)],
    y=[("z", 3)],
    v=[("z", 3)])

def get_successors(node):
    if node[0] == "direct":
        _, x, z = node
        succ = Nil
        if x in stateS and z in stateU:
            for y in borders:
                succ = Cons((("via", x, z, y), 0), succ)
        if x in distances:
            for y, d in distances[x]:
                succ = Cons((("direct", y, z), d), succ)
        if succ == Nil:
            return None
        return ("or", succ)
    if node[0] == "via":
        _, x, z, y = node
        return ("and", LinkedList([(("direct", x, y), 0), (("direct", y, z), 0)]))

def is_goal(node):
    return node[0] == "direct" and node[1] == node[2]

def h(node):
    if is_goal(node):
        return 0
    if node[0] == "direct":
        _, x, z = node
        if x in distances:
            for y, d in distances[x]:
                if y == z:
                    return d
        if x in stateS and z in stateU or z in stateS and x in stateU:
            return 2
        return 1
    if node[0] == "via":
        _, x, z, _ = node
        if x in stateS and z in stateU or z in stateS and x in stateU:
            return 2


# demonstracni vypis
if __name__ == "__main__":
    print("Cesta mezi mesty, algoritmus AND/OR A*\n")
    print("Zadani: %s" % (start,))

    print("\nNalezene reseni:")
    obj = BestSearch(biggest, is_goal, get_successors, h)
    solution = obj.search(start)
    print("Prohledano %d stavu, vysledne reseni ma cenu %d." % (obj.total, solution[2]))
    print(solution)
