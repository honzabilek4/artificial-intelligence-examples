#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

nil = None

def addleaf(tree, x):
    if tree == nil:
        return (nil, x, nil)
    left, root, right = tree
    if x == root:
        return tree
    if root > x:
        return (addleaf(left, x), root, right)
    else:
        return (left, root, addleaf(right, x))

def delleaf(tree, x):
    if tree == nil:
        return nil
    left, root, right = tree
    if x == root:
        if left == nil:
            return right
        if right == nil:
            return left
        right1, y = delmin(right, x)
        return (left, y, right1)
    if root > x:
        return (delleaf(left, x), root, right)
    else:
        return (left, root, delleaf(right, x))

def delmin(tree, x):
    if tree == nil:
        raise ValueError("delmin je treba volat nad neprazdnym stromem")
    left, root, right = tree
    if left == nil:
        return (right, root)
    left1, y = delmin(left, x)
    return ((left1, root, right), y)

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
    print("T = addleaf(nil, 6); T1 = addleaf(T, 8); T2 = addleaf(T1, 2); " +
          "T3 = addleaf(T2, 4); T4 = addleaf(T3, 1); show(T4) :")
    T = addleaf(nil, 6)
    T1 = addleaf(T, 8)
    T2 = addleaf(T1, 2)
    T3 = addleaf(T2, 4)
    T4 = addleaf(T3, 1)
    show(T4)

    print("\nSmazani uzlu s hodnotou 8:")
    print("T5 = delleaf(T4, 8); show(T5) :")
    T5 = delleaf(T4, 8)
    show(T5)

    print("\nSmazani uzlu s hodnotou 2:")
    print("T6 = delleaf(T5, 2); show(T6) :")
    T6 = delleaf(T5, 2)
    show(T6)
