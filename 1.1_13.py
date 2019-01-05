#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

# fakty (DB)
# klici hasove tabulky jsou jmena potomku, hodnotami jmena rodicu
otec = dict(dana="milan", petr="milan", david="jan")
matka = dict(dana="pavla", petr="pavla", david="jana")
potomci = set(list(otec.keys()) + list(matka.keys()))

# pravidla
def rodic(x, y):
    return y in otec and otec[y] == x or \
        y in matka and matka[y] == x

def rodic_anyX(y):
    xs = []
    if y in otec:
        xs.append(otec[y])
    if y in matka:
        xs.append(matka[y])
    return xs

def sourozenci(x, y):
    return x in otec and y in otec and otec[x] == otec[y] and x != y and \
        x in matka and y in matka and matka[x] == matka[y]

def sourozenci_anyY(x):
    ys = []
    for y in potomci:
        if sourozenci(x, y):
            ys.append(y)
    return ys

# demonstracni vypis
if __name__ == "__main__":
    print("Vysledek dotazu otec['dana'] je '%s'." % otec["dana"])
    print("Vysledek dotazu rodic_anyX('david') je %s." % \
            rodic_anyX("david"))
    print("Vysledek dotazu sourozenci_anyY('dana') je %s." % \
            sourozenci_anyY("dana"))
