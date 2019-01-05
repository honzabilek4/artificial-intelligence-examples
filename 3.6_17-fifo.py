#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from collections import deque
from linked_lists import Cons, Nil

def solution(node):
    for path in breadth_first_search(node):
        yield path

def breadth_first_search(start_node):
    paths = deque([Cons(start_node, Nil)]) # pouzijeme pythonovskou frontu jako FIFO
    while len(paths) > 0:
        path = paths.popleft()
        node = path.head
        if is_goal(node):
            yield path
        for node1 in move_anyY(node):
            paths.append(Cons(node1, path))

def is_goal(x):
    # zavisi na resenem problemu
    return x == "E"

graph = dict(A=["B", "E", "F"],
             B=["C"], F=["C"],
             C=["D"],
             D=["E"])

def move_anyY(x):
    # zavisi na resenem problemu
    if x in graph:
        for y in graph[x]:
            yield y

# demonstracni vypis
if __name__ == "__main__":
    print("Breadth-First Search")
    print("Volani next(solution('A')) : %s" % next(solution('A')))
