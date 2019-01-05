#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import LinkedList, Cons, Nil

def solution(node):
    for path in breadth_first_search(LinkedList([LinkedList(node)])):
        yield path

def breadth_first_search(paths):
    path = paths.head
    node = path.head
    if is_goal(node):
        yield path
    new_paths = Nil
    for node1 in move_anyY(node):
        if not member(node1, path):
            new_paths = Cons(Cons(node1, path), new_paths)
    if new_paths != Nil:
        paths1 = append(paths.tail, new_paths)
    else:
        paths1 = paths.tail
    for path in breadth_first_search(paths1):
        yield path

def append(xs, ys):
    if xs == Nil:
        return ys
    else:
        return Cons(xs.head, append(xs.tail, ys))

def member(x, xs):
    if xs == Nil:
        return False
    if x == xs.head:
        return True
    return member(x, xs.tail)

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
