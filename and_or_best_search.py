#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

""" Implementace algoritmu AND/OR A* """

from linked_lists import Cons, Nil

class BestSearch(object):
    def __init__(self, bound, is_goal, get_successors, h):
        self.total = 0
        self.bound = bound
        self.is_goal = is_goal
        self.get_successors = get_successors
        self.h = h

    def search(self, start):
        self.total = 0
        sol, solved = self.expand(("leaf", start, 0, 0), self.bound)
        if solved == "yes":
            return sol
        else:
            raise ValueError("Reseni neexistuje.")

    def expand(self, tree, bound):
        if f(tree) > bound:
            return (tree, "no")
        tree_type = tree[0]
        if tree_type == "leaf":
            self.total = self.total + 1
            _, node, f_, c = tree
            if self.is_goal(node):
                return (("solved_leaf", node, f_), "yes")
            tree1 = self.expandnode(node, c)
            if tree1 is None: # neexistuji naslednici
                return (None, "never")
            return self.expand(tree1, bound)
        elif tree_type == "tree":
            _, node, f_, c, subtrees = tree
            newsubs, solved1 = self.expandlist(subtrees, bound-c)
            return self.continue_(solved1, node, c, newsubs, bound)

    def expandlist(self, trees, bound):
        tree, othertrees, bound1 = select_tree(trees, bound)
        newtree, solved = self.expand(tree, bound1)
        return combine(othertrees, newtree, solved)

    def continue_(self, subtr_solved, node, c, subtrees, bound):
        if subtr_solved == "never":
            return (None, "never")
        h_ = bestf(subtrees)
        f_ = c + h_
        if subtr_solved == "yes":
            return (("solved_tree", node, f_, subtrees), "yes")
        if subtr_solved == "no":
            return self.expand(("tree", node, f_, c, subtrees), bound)

    def expandnode(self, node, c):
        succ = self.get_successors(node)
        if succ is None:
            return None
        op, successors = succ
        subtrees = self.evaluate(successors)
        h_ = bestf((op, subtrees))
        f_ = c + h_
        return ("tree", node, f_, c, (op, subtrees))

    def evaluate(self, nodes):
        if nodes == Nil:
            return Nil
        node, c = nodes.head
        h_ = self.h(node)
        f_ = c + h_
        trees1 = self.evaluate(nodes.tail)
        trees = insert(("leaf", node, f_, c), trees1)
        return trees

def combine(subtrees, tree, solved):
    op, trees = subtrees
    if op == "or":
        if solved == "yes":
            return (("or_result", tree), "yes")
        if solved == "no":
            newtrees = insert(tree, trees)
            return (("or", newtrees), "no")
        if solved == "never":
            if trees == Nil:
                return (None, "never")
            return (("or", trees), "no")
    if op == "and":
        if solved == "yes" and are_all_solved(trees):
            return (("and_result", Cons(tree, trees)), "yes")
        if solved == "never":
            return (None, "never")
        newtrees = insert(tree, trees)
        return (("and", newtrees), "no")

def f(tree):
    return tree[2]

def are_all_solved(trees):
    if trees == Nil:
        return True
    return is_solved(trees.head) and are_all_solved(trees.tail)

def is_solved(tree):
    tree_type = tree[0]
    return tree_type == "solved_tree" or tree_type == "solved_leaf"

def insert(t, trees):
    if trees == Nil:
        return Cons(t, Nil)
    t1 = trees.head
    ts = trees.tail
    if is_solved(t1):
        return Cons(t, trees)
    if is_solved(t):
        return Cons(t1, insert(t, ts))
    if f(t) <= f(t1):
        return Cons(t, trees)
    return Cons(t1, insert(t, ts))

def bestf(subtrees):
    op = subtrees[0]
    if op == "or":
        trees = subtrees[1]
        assert trees != Nil
        return f(trees.head)
    if op == "and" or op == "and_result":
        trees = subtrees[1]
        if trees == Nil:
            return 0
        return f(trees.head) + bestf(("and", trees.tail))
    if op == "or_result":
        tree = subtrees[1]
        return f(tree)

def select_tree(subtrees, bound):
    op, trees = subtrees
    if trees.tail == Nil:
        return (trees.head, (op, Nil), bound)
    f_ = bestf((op, trees.tail))
    assert op == "or" or op == "and"
    if op == "or":
        bound1 = min(bound, f_)
    if op == "and":
        bound1 = bound - f_
    return (trees.head, (op, trees.tail), bound1)
