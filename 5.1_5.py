#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import LinkedList, Cons, Nil

hanoi_mem = dict()
def hanoi(n, a, b, c):
    if n == 1:
        return LinkedList(["%s to %s" % (a, b)])
    if n < 1:
        raise ValueError("n musi byt kladne")
    if (n+1, a, c, b) not in hanoi_mem:
        hanoi_mem[(n-1, a, c, b)] = hanoi(n-1, a, c, b)
    if (n+1, a, c, b) not in hanoi_mem:
        hanoi_mem[(n-1, c, b, a)] = hanoi(n-1, c, b, a)
    ms1 = hanoi_mem[(n-1, a, c, b)]
    ms2 = hanoi_mem[(n-1, c, b, a)]
    return append(ms1, Cons("%s to %s" % (a, b), ms2))

def append(xs, ys):
    if xs == Nil:
        return ys
    else:
        return Cons(xs.head, append(xs.tail, ys))

# demonstracni vypis
if __name__ == "__main__":
    print("Demonstrace programu Hanoi")
    print("hanoi(pocet_taliru, z_tyce, na_tyc, pomoci_tyce)")

    print("\nVysledek dotazu hanoi(2, 'a', 'b', 'c'): ")
    print(hanoi(2, 'a', 'b', 'c'))

    print("\nVysledek dotazu hanoi(3, 'a', 'b', 'c'): ")
    print(hanoi(3, 'a', 'b', 'c'))

    print("\nVysledek dotazu hanoi(4, 'a', 'b', 'c'): ")
    print(hanoi(4, 'a', 'b', 'c'))
