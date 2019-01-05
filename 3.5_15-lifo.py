#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import Cons, Nil

def solution(node):
    for path in depth_first_search(node, 999):
        yield path

def depth_first_search(start_node, max_depth):
    paths = [(Cons(start_node, Nil), max_depth)] # pouzijeme pythonovsky seznam jako LIFO
    while len(paths) > 0:
        path, remaining_depth = paths.pop()
        node = path.head
        if is_goal(node):
            yield path
        if remaining_depth > 0:
            for node1 in move_anyY(node):
                paths.append((Cons(node1, path), remaining_depth-1))

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
    print("Depth-First Search")
    print("Volani next(solution('A')) : %s" % next(solution('A')))
    print("Volani next(depth_first_search('A', 3)) : %s" % \
            next(depth_first_search('A', 3)))
    print("Volani next(depth_first_search('A', 4)) : %s" % \
            next(depth_first_search('A', 4)))
