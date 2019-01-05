#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import LinkedList, Cons, Nil

graph = dict(
    a=("or", LinkedList(["b", "c"])),
    b=("and", LinkedList(["d", "e"])),
    c=("and", LinkedList(["f", "g"])),
    e=("or", LinkedList(["h"])),
    f=("and", LinkedList(["h", "i"])))

goals = dict(d=True, g=True, h=True)

def is_goal(node):
    # zavisi na resenem problemu
    return node in goals

def solve(node):
    if is_goal(node):
        yield node
    if node in graph:
        nodes = graph[node][1]
        if graph[node][0] == "or":
            for node1 in member_anyX(nodes):
                for tree in solve(node1):
                    yield (node, "--->", tree)
        elif graph[node][0] == "and":
            for trees in solveall(nodes):
                yield (node, "--->", ("and", trees))

def solveall(nodes):
    if nodes == Nil:
        yield Nil
    else:
        for tree in solve(nodes.head):
            for trees in solveall(nodes.tail):
                yield Cons(tree, trees)

def member_anyX(xs):
    if xs == Nil:
        return
    yield xs.head
    for x in member_anyX(xs.tail):
        yield x

# demonstracni vypis
if __name__ == "__main__":
    print('Prohledavani AND/OR grafu')
    print('\n  Graf:')
    print('    a ---> or:[b,c].')
    print('    b ---> and:[d,e].')
    print('    c ---> and:[f,g].')
    print('    e ---> or:[h].')
    print('    f ---> and:[h,i].')
    print('    goal(d).')
    print('    goal(g).')
    print('    goal(h).')
    print('\nVysledky dotazu solve("a"):')
    for solution in solve("a"):
        print(solution)
