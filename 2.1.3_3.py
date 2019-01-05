#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import LinkedList, Nil

def member(x, ys):
    if ys == Nil:
        return False
    if x == ys.head:
        return True
    return member(x, ys.tail)

# demonstracni vypis
if __name__ == "__main__":
    print("Member - 3. varianta")
    print("Vysledek volani member('a', LinkedList(['a', 'b', 'a'])) je %s." % \
            member("a", LinkedList(["a", "b", "a"])))
