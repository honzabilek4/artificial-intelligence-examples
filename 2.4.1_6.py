#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import LinkedList, Cons, Nil

def append(xs, ys):
    if xs == Nil:
        return ys
    else:
        return Cons(xs.head, append(xs.tail, ys))

def append_anyXs(ys, zs):
    if ys == zs:
        return Nil
    if zs == Nil:
        raise ValueError("ys neni sufixem zs")
    return Cons(zs.head, append_anyXs(ys, zs.tail))

def append_anyXsYs(zs):
    yield ([], zs)
    if zs != Nil:
        for xs, ys in append_anyXsYs(zs.tail):
            yield (Cons(zs.head, xs), ys)

# demonstracni vypis
if __name__ == "__main__":
    print("Prace se seznamy - append")
    print("-------------------------------\n")
    print("vicesmerne implementace funkce append:\n")
    print("Vysledek volani append(LinkedList(['a', 'b']), LinkedList(['c', 'd'])): \n\t%s\n" % \
            append(LinkedList(['a', 'b']), LinkedList(['c', 'd'])))

    print("Vysledek volani append_anyXs(LinkedList(['c', 'd'])," +
          "LinkedList(['a', 'b', 'c', 'd'])): \n\t%s\n" % \
            append_anyXs(LinkedList(['c', 'd']), LinkedList(['a', 'b', 'c', 'd'])))

    print("Vysledek volani append_anyXsYs(LinkedList(['a', 'b', 'c'])): \n\t%s\n" % \
            list(append_anyXsYs(LinkedList(['a', 'b', 'c']))))
