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
    print("Vysledek volani")
    print("T = addleaf(nil, 6); T1 = addleaf(T, 8); T2 = addleaf(T1, 2); " +
          "T3 = addleaf(T2, 4); T4 = addleaf(T3, 1); show(T4) :")
    T = addleaf(nil, 6)
    T1 = addleaf(T, 8)
    T2 = addleaf(T1, 2)
    T3 = addleaf(T2, 4)
    T4 = addleaf(T3, 1)
    show(T4)

    print("\nVysledek volani")
    print("T5 = addleaf((((nil, 1, nil), 2, ((nil, 3, nil), 4, (nil, 5, nil))), " +
          "6, ((nil, 7, nil), 8, (nil, 9, nil))), 10); show(T5) :")
    T5 = addleaf((((nil, 1, nil), 2, ((nil, 3, nil), 4, (nil, 5, nil))),
                  6, ((nil, 7, nil), 8, (nil, 9, nil))), 10)
    show(T5)
