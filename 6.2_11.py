#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

# je zapotrebi nainstaloval balicek python-constraint
# <https://github.com/python-constraint/python-constraint>
from constraint import Problem, AllDifferentConstraint

problem = Problem()
domain = range(10)
variables = ("S", "E", "N", "D", "M", "O", "R", "Y")
for name in variables:
    problem.addVariable(name, domain)
problem.addConstraint(lambda s: s > 0, ("S"))
problem.addConstraint(lambda m: m > 0, ("M"))
problem.addConstraint(AllDifferentConstraint())
problem.addConstraint(lambda s, e, n, d, m, o, r, y: \
                      1000 * s + 100 * e + 10 * n + d +
                      1000 * m + 100 * o + 10 * r + e ==
                      10000 * m + 1000 * o + 100 * n + 10 * e + y, variables)

# demonstracni vypis
if __name__ == "__main__":
    print("CLP - Algebrogram\n")

    print("  S E N D")
    print("+ M O R E")
    print("---------")
    print("M O N E Y\n")

    print("Vysledek volani problem.getSolutions():")
    solution = problem.getSolutions()[0]
    print(" S = %s, E = %s, N = %s, D = %s, M = %s, O = %s, R = %s, Y = %s" % \
            tuple((solution[x] for x in variables)))
