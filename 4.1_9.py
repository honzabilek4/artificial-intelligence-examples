#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import Cons, Nil
from romanian_cities import graph

# horni zavora pro cenu nejlepsi cesty
biggest = 9999

def best_search(start):
    for _, solved, sol in expand(Nil, (start, 0, 0), biggest):
        if solved == "yes":
            yield sol

def expand(path, tree, bound):
    if len(tree) == 3: # a leaf
        node, f_, g = tree
        if is_goal(node):
            yield (None, "yes", (f_, Cons(node, path)))
        if f_ <= bound:
            succ = Nil
            for m, c in move_anyYC(node):
                if not member(m, path):
                    succ = Cons((m, c), succ)
            if succ == Nil:
                yield (None, "never", None)
            else:
                trees = succlist(g, succ)
                f1 = bestf(trees)
                for tree1, solved, sol in expand(path, (node, f1, g, trees), bound):
                    yield (tree1, solved, sol)
        elif f_ > bound:
            yield (tree, "no", None)
    else: # a tree
        node, f_, g, trees = tree
        if trees == Nil:
            yield (None, "never", None)
        else:
            if f_ <= bound:
                bound1 = min(bound, bestf(trees.tail))
                for t1, solved1, sol1 in expand(Cons(node, path), trees.head, bound1):
                    for tree1, solved, sol in continue_(path, (node, f_, g, Cons(t1, trees.tail)),
                                                        bound, solved1, sol1):
                        yield (tree1, solved, sol)
            elif f_ > bound:
                yield (tree, "no", None)

def continue_(path, tree, bound, subtr_solved, sol):
    node, _, g, trees = tree
    if subtr_solved == "yes":
        yield (None, "yes", sol)
    elif subtr_solved == "no":
        nts = insert(trees.head, trees.tail)
        f1 = bestf(nts)
        for tree1, solved, sol in expand(path, (node, f1, g, nts), bound):
            yield (tree1, solved, sol)
    elif subtr_solved == "never":
        f1 = bestf(trees.tail)
        for tree1, solved, sol in expand(path, (node, f1, g, trees.tail), bound):
            yield (tree1, solved, sol)

def succlist(g0, succ):
    if succ == Nil:
        return Nil
    n, c = succ.head
    g = g0 + c
    f_ = g + h(n)
    ts1 = succlist(g0, succ.tail)
    ts = insert((n, f_, g), ts1)
    return ts

def f(tree):
    if len(tree) == 3: # a leaf
        _, f_, _ = tree
    else: # a tree
        _, f_, _, _ = tree
    return f_

def bestf(trees):
    if trees == Nil:
        return biggest
    return f(trees.head)

def insert(t, ts):
    if f(t) <= bestf(ts):
        return Cons(t, ts)
    return Cons(ts.head, insert(t, ts.tail))

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
    print("Best-First Search (algoritmus A*)")
    print("Veskere jednoduche cesty mezi mesty Arad a Bukurest serazene vzestupne podle ceny:")
    for solution in best_search('Arad'):
        print(solution)
