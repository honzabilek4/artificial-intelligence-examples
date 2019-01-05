#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

import heapq
from linked_lists import Cons, Nil
from romanian_cities import graph

# horni zavora pro cenu nejlepsi cesty
biggest = 9999

def best_search(start):
    heap = [(0, 0, start, Nil)]
    while True:
        try:
            f, g, node, path = heapq.heappop(heap)
        except IndexError: # fronta je prazdna
            break
        path1 = Cons(node, path)
        if is_goal(node):
            yield (f, path1)
        if f <= biggest:
            for m, c in move_anyYC(node):
                if not member(m, path1):
                    heapq.heappush(heap, (g+c+h(m), g+c, m, path1))

def member(x, xs):
    if xs == Nil:
        return False
    if x == xs.head:
        return True
    return member(x, xs.tail)

def is_goal(x):
    # zavisi na resenem problemu
    return x == "Bukurest"

def move_anyYC(x):
    # zavisi na resenem problemu
    if x in graph:
        for y, c in graph[x][0]:
            yield (y, c)

def h(x):
    # zavisi na resenem problemu
    return graph[x][1]

# demonstracni vypis
if __name__ == "__main__":
    print("Best-First Search (algoritmus A*) - implementace pomoci prioritni fronty")
    print("Veskere jednoduche cesty mezi mesty Arad a Bukurest serazene vzestupne podle ceny:")
    for solution in best_search('Arad'):
        print(solution)
