#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import Cons, Nil

def solution(node):
    for path in depth_first_search(Nil, node, 999):
        yield path

def depth_first_search(akumulator_path, node, remaining_depth):
    akumulator_path1 = Cons(node, akumulator_path)
    if is_goal(node):
        yield akumulator_path1
    if remaining_depth > 0:
        for node1 in move_anyY(node):
            for path in depth_first_search(akumulator_path1, node1,
                                           remaining_depth-1):
                yield path

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
    print("Volani next(depth_first_search(Nil, 'A', 3)) : %s" % \
            next(depth_first_search(Nil, 'A', 3)))
    print("Volani next(depth_first_search(Nil, 'A', 4)) : %s" % \
            next(depth_first_search(Nil, 'A', 4)))
