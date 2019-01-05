#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

""" Implementace algoritmu A* """

from linked_lists import Cons, Nil

class BestSearch(object):
    def __init__(self, bound, is_goal, move_anyYC, h):
        self.total = 0
        self.bound = bound
        self.is_goal = is_goal
        self.move_anyYC = move_anyYC
        self.h = h

    def search(self, start):
        self.total = 0
        for _, solved, sol in self.expand(Nil, (start, 0, 0), self.bound):
            if solved == "yes":
                yield sol

    def expand(self, path, tree, bound):
        if len(tree) == 3: # a leaf
            node, f_, g = tree
            if self.is_goal(node):
                yield (None, "yes", Cons(node, path))
            if f_ <= bound:
                succ = Nil
                for m, c in self.move_anyYC(node):
                    if not member(m, path):
                        self.total = self.total + 1
                        succ = Cons((m, c), succ)
                if succ == Nil:
                    yield (None, "never", None)
                else:
                    trees = self.succlist(g, succ)
                    f1 = self.bestf(trees)
                    for tree1, solved, sol in self.expand(path, (node, f1, g, trees), bound):
                        yield (tree1, solved, sol)
            elif f_ > bound:
                yield (tree, "no", None)
        else: # a tree
            node, f_, g, trees = tree
            if trees == Nil:
                yield (None, "never", None)
            else:
                if f_ <= bound:
                    bound1 = min(bound, self.bestf(trees.tail))
                    for t1, solved1, sol1 in self.expand(Cons(node, path), trees.head, bound1):
                        for tree1, solved, sol in self.continue_(path, (node, f_, g,
                                                                        Cons(t1, trees.tail)),
                                                                 bound, solved1, sol1):
                            yield (tree1, solved, sol)
                elif f_ > bound:
                    yield (tree, "no", None)

    def continue_(self, path, tree, bound, subtr_solved, sol):
        node, _, g, trees = tree
        if subtr_solved == "yes":
            yield (None, "yes", sol)
        elif subtr_solved == "no":
            nts = self.insert(trees.head, trees.tail)
            f1 = self.bestf(nts)
            for tree1, solved, sol in self.expand(path, (node, f1, g, nts), bound):
                yield (tree1, solved, sol)
        elif subtr_solved == "never":
            f1 = self.bestf(trees.tail)
            for tree1, solved, sol in self.expand(path, (node, f1, g, trees.tail), bound):
                yield (tree1, solved, sol)

    def succlist(self, g0, succ):
        if succ == Nil:
            return Nil
        n, c = succ.head
        g = g0 + c
        f_ = g + self.h(n)
        ts1 = self.succlist(g0, succ.tail)
        ts = self.insert((n, f_, g), ts1)
        return ts

    def bestf(self, trees):
        if trees == Nil:
            return self.bound
        return f(trees.head)

    def insert(self, t, ts):
        if f(t) <= self.bestf(ts):
            return Cons(t, ts)
        return Cons(ts.head, self.insert(t, ts.tail))

def f(tree):
    if len(tree) == 3: # a leaf
        _, f_, _ = tree
    else: # a tree
        _, f_, _, _ = tree
    return f_

def member(x, xs):
    if xs == Nil:
        return False
    if x == xs.head:
        return True
    return member(x, xs.tail)
