#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import LinkedList, Cons, Nil

def append(xs, ys):
    if xs == Nil:
        return ys
    else:
        return Cons(xs.head, append(xs.tail, ys))

def qsort(xs):
    if xs == Nil:
        return Nil
    if xs.tail == Nil:
        return xs
    ms, vs = divide(xs.head, xs.tail)
    return append(qsort(ms), Cons(xs.head, qsort(vs)))

def divide(h, xs):
    if xs == Nil:
        return (Nil, Nil)
    ms, vs = divide(h, xs.tail)
    if xs.head <= h:
        return (Cons(xs.head, ms), vs)
    else:
        return (ms, Cons(xs.head, vs))

# demonstracni vypis
if __name__ == "__main__":
    print("Radici algoritmus QuickSort\n")
    print("qsort(LinkedList([5, 2, 8, 2, 654, 8, 3, 4])): \n\t%s\n" % \
            qsort(LinkedList([5, 2, 8, 2, 654, 8, 3, 4])))
