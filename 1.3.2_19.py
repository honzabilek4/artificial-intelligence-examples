#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

fib_mem = dict()
def fib(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if not x in fib_mem:
        fib_mem[x] = fib(x-1) + fib(x-2)
    return fib_mem[x]

# demonstracni vypis
if __name__ == "__main__":
    print("Program pro vypocet clenu fibonacciho posloupnosti, " + \
       "efektivnejsi varianta.")
    print('Vysledek volani fib(36) je %d.' % fib(36))
