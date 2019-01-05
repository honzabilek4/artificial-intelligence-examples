#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import LinkedList, Cons, Nil

def del1_anyX(ys):
    if ys == Nil:
        return
    yield (ys.head, ys.tail)
    for (z, zs) in del1_anyX(ys.tail):
        yield (z, Cons(ys.head, zs))

def insert(x, ys):
    yield Cons(x, ys)
    if not ys == Nil:
        for zs in insert(x, ys.tail):
            yield Cons(ys.head, zs)

def perm1(xs):
    if xs == Nil:
        yield Nil
    else:
        for ys in perm1(xs.tail):
            for zs in insert(xs.head, ys):
                yield zs

def perm2(xs):
    if xs == Nil:
        yield Nil
    else:
        for y, ys in del1_anyX(xs):
            for zs in perm2(ys):
                yield Cons(y, zs)

def perm3(xs):
    if xs == Nil:
        yield Nil
    else:
        ys = Nil
        while xs != Nil:
            result = xs.tail
            for y in ys:
                result = Cons(y, result)
            for zs in perm3(result):
                yield Cons(xs.head, zs)
            ys = Cons(xs.head, ys)
            xs = xs.tail

# demonstracni vypis
if __name__ == "__main__":
    print("Prace se seznamy - permutace")
    print("-------------------------------\n")
    print("perm1 napsany pomoci insert")
    print("Vysledek volani perm1(LinkedList([1, 2, 3])): \n\t%s\n" % \
            list(perm1(LinkedList([1, 2, 3]))))

    print("perm2 napsany pomoci del1_anyX")
    print("Vysledek volani perm2(LinkedList([1, 2, 3])): \n\t%s\n" % \
            list(perm2(LinkedList([1, 2, 3]))))

    print("perm3 napsany pomoci pruchodu seznamem")
    print("Vysledek volani perm3(LinkedList([1, 2, 3])): \n\t%s\n" % \
            list(perm3(LinkedList([1, 2, 3]))))
