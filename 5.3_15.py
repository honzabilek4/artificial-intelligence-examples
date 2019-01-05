#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import LinkedList, Cons, Nil

# horni zavora pro cenu nejlepsi cesty
biggest = 9999

# format uzlu: ("leaf", n, f, c)
#              ("tree", n, f, c, subtrees)
#              ("solved_leaf", n, f)
#              ("solved_tree", n, f, subtrees)

# format seznamu potomku:
#              ("and", trees)
#              ("or", trees)
#              ("and_result", trees)
#              ("or_result", tree)

def andor(node):
    sol, solved = expand(("leaf", node, 0, 0), biggest)
    if solved == "yes":
        return sol
    else:
        raise ValueError("Reseni neexistuje.")

def expand(tree, bound):
    if f(tree) > bound:
        return (tree, "no")
    tree_type = tree[0]
    if tree_type == "leaf":
        _, node, f_, c = tree
        if is_goal(node):
            return (("solved_leaf", node, f_), "yes")
        tree1 = expandnode(node, c)
        if tree1 is None: # neexistuji naslednici
            return (None, "never")
        return expand(tree1, bound)
    elif tree_type == "tree":
        _, node, f_, c, subtrees = tree
        newsubs, solved1 = expandlist(subtrees, bound-c)
        return continue_(solved1, node, c, newsubs, bound)

def expandlist(trees, bound):
    tree, othertrees, bound1 = select_tree(trees, bound)
    newtree, solved = expand(tree, bound1)
    return combine(othertrees, newtree, solved)

def continue_(subtr_solved, node, c, subtrees, bound):
    if subtr_solved == "never":
        return (None, "never")
    h_ = bestf(subtrees)
    f_ = c + h_
    if subtr_solved == "yes":
        return (("solved_tree", node, f_, subtrees), "yes")
    if subtr_solved == "no":
        return expand(("tree", node, f_, c, subtrees), bound)

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

def expandnode(node, c):
    succ = get_successors(node)
    if succ is None:
        return None
    op, successors = succ
    subtrees = evaluate(successors)
    h_ = bestf((op, subtrees))
    f_ = c + h_
    return ("tree", node, f_, c, (op, subtrees))

def evaluate(nodes):
    if nodes == Nil:
        return Nil
    node, c = nodes.head
    h_ = h(node)
    f_ = c + h_
    trees1 = evaluate(nodes.tail)
    trees = insert(("leaf", node, f_, c), trees1)
    return trees

def are_all_solved(trees):
    if trees == Nil:
        return True
    return is_solved(trees.head) and are_all_solved(trees.tail)

def is_solved(tree):
    tree_type = tree[0]
    return tree_type == "solved_tree" or tree_type == "solved_leaf"

def f(tree):
    return tree[2]

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

def h(_):
    # zavisi na resenem problemu
    return 0

graph = dict(
    a=("or", LinkedList([("b", 1), ("c", 3)])),
    b=("and", LinkedList([("d", 1), ("e", 1)])),
    c=("and", LinkedList([("f", 2), ("g", 1)])),
    e=("or", LinkedList([("h", 6)])),
    f=("or", LinkedList([("h", 2), ("i", 3)])))

goals = dict(d=True, g=True, h=True)

def is_goal(node):
    # zavisi na resenem problemu
    return node in goals

# tato funkce nahrazuje prologovska fakta tvaru node ---> Op:Subtrees
# a pro zadany node navraci prislusne Op:Subtrees
def get_successors(node):
    # zavisi na resenem problemu
    if node in graph:
        return graph[node]
    return None

# demonstracni vypis
if __name__ == "__main__":
    print('Prohledavani AND/OR grafu')
    print('\n  Graf:')
    print('    a ---> or:[b/1,c/3].')
    print('    b ---> and:[d/1,e/1].')
    print('    c ---> and:[f/2,g/1].')
    print('    e ---> or:[h/6].')
    print('    f ---> or:[h/2,i/3].')
    print('    h(X,0).')
    print('    goal(d).')
    print('    goal(g).')
    print('    goal(h).')
    print('\nVysledky dotazu andor("a"):')
    print(andor("a"))
