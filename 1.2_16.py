#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

def tiskniseznam(xs):
    i = 1
    print("seznam=[")
    while xs != None:
        print("    %d: %s" % (i, xs[0]))
        i = i + 1
        xs = xs[1]
    print("]")

# demonstracni vypis
if __name__ == "__main__":
    print("Program vytiskne zadany seznam. Napr.:\n")
    print("Vysledek volani tiskniseznam(('a', ('b', ('c', None)))) je:\n")
    tiskniseznam(('a', ('b', ('c', None))))

    print("\n\nVysledek volani tiskniseznam(('a', ('b', (['c1', 'c2', 'c3'], " +
          "('d', ('mezi d a e', ('e', None))))))). je:\n")
    tiskniseznam(('a', ('b', (['c1', 'c2', 'c3'], ('d', ('mezi d a e', ('e', None)))))))
    print("")
