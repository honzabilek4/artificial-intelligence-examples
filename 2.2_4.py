#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import LinkedList, Cons, Nil

def del_(x, ys):
    if ys == Nil:
        return Nil
    if x == ys.head:
        return del_(x, ys.tail)
    return Cons(ys.head, del_(x, ys.tail))

def del1(x, ys):
    if ys == Nil:
        return
    if x == ys.head:
        yield ys.tail
    for zs in del1(x, ys.tail):
        yield Cons(ys.head, zs)

def insert(x, ys):
    yield Cons(x, ys)
    if not ys == Nil:
        for zs in insert(x, ys.tail):
            yield Cons(ys.head, zs)

def insert1(x, ys):
    return Cons(x, ys)

# demonstracni vypis
if __name__ == "__main__":
    print("Prace se seznamy - del a insert")
    print("-------------------------------\n")
    print("funkce del_(x, ys) smaze vsechny vyskyty prvku x ze seznamu ys")
    print("Vysledek volani del_(1, LinkedList([1, 2, 1, 1, 2, 3, 1, 1])):\n\t%s\n" % \
            del_(1, LinkedList([1, 2, 1, 1, 2, 3, 1, 1])))

    print("del1(x, ys) smaze vzdy jeden (podle poradi) vyskyt prvku x v seznamu ys")
    print("Vysledek volani del1(1, LinkedList([1, 2, 1])): \n\t%s\n" % \
            list(del1(1, LinkedList([1, 2, 1]))))

    print("insert(x, ys) vklada postupne na vsechny pozice seznamu ys prvek x")
    print("Vysledek volani insert(4, LinkedList([2, 3, 1])): \n\t%s\n" % \
            list(insert(4, LinkedList([2, 3, 1]))))

    print("insert1(x, ys) vlozi x na zacatek seznamu ys")
    print("Vysledek volani insert1(4, LinkedList([2, 3, 1])): \n\t%s\n" % \
            insert1(4, LinkedList([2, 3, 1])))
