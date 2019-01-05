#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

nil = None

def add(tree, x):
    yield addroot(tree, x)
    if tree == nil:
        return
    left, y, right = tree
    if y > x:
        yield (add(left, x), y, right)
    else:
        yield (left, y, add(right, x))

def addroot(tree, x):
    if tree == nil:
        return (nil, x, nil)
    left, y, right = tree
    if y > x:
        left1, _, left2 = addroot(left, x)
        return (left1, x, (left2, y, right))
    if y < x:
        right1, _, right2 = addroot(right, x)
        return ((left, y, right1), x, right2)
    return tree

def del_(tree, x):
    if tree == nil:
        return
    for tree1 in delroot(tree, x):
        yield tree1
    left, y, right = tree
    if y > x:
        for left1 in del_(left, x):
            yield (left1, y, right)
    else:
        for right1 in del_(right, x):
            yield (left, y, right1)

def delroot(tree, x):
    if tree == nil:
        return
    tree_left, tree_y, tree_right = tree
    if tree_y != x:
        return
    if tree_left == nil and tree_right == nil:
        yield nil
    if tree_right != nil:
        left1 = tree_left
        left2, y, right = tree_right
        if y > x:
            for left in delroot((left1, x, left2), x):
                yield (left, y, right)
    if tree_left != nil:
        left, y, right1 = tree_left
        right2 = tree_right
        if y < x:
            for right in delroot((right1, x, right2), x):
                yield (left, y, right)
    yield tree

def show(tree):
    show2(tree, 0)

def show2(tree, indent):
    if tree == nil:
        return
    left, root, right = tree
    show2(right, indent+2)
    print("%s%s" % (" " * indent, root))
    show2(left, indent+2)

# demonstracni vypis
if __name__ == "__main__":
    print("Binarni stromy")
    print("--------------\n")
    print("Vytvoreni stromu:")
    print("T = next(add(nil, 6)); T1 = next(add(T, 8)); T2 = next(add(T1, 2)); " +
          "T3 = next(add(T2, 4)); T4 = next(add(T3, 1)); show(T4) :")
    T = next(add(nil, 6))
    T1 = next(add(T, 8))
    T2 = next(add(T1, 2))
    T3 = next(add(T2, 4))
    T4 = next(add(T3, 1))
    show(T4)

    print("\nSmazani uzlu s hodnotou 8:")
    print("T5 = next(del_(T4, 8)); show(T5) :")
    T5 = next(del_(T4, 8))
    show(T5)

    print("\nSmazani uzlu s hodnotou 2:")
    print("T6 = next(del_(T5, 2)); show(T6) :")
    T6 = next(del_(T5, 2))
    show(T6)
