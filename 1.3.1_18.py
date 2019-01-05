#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

def fib(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fib(x-1) + fib(x-2)

# demonstracni vypis
if __name__ == "__main__":
    print("Program pro vypocet clenu fibonacciho posloupnosti, " + \
       "mene efektivni varianta (vypocet potrva nekolik vterin).")
    print('Vysledek volani fib(36) je %d.' % fib(36))
