#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

# je zapotrebi nainstaloval balicek python-constraint
from constraint import Problem
from linked_lists import LinkedList, Nil

def queens(n):
    problem = Problem()
    domain = range(n+1)[1:]
    variables = LinkedList(list("X%d" % i for i in range(n+1)[1:]))
    for name in variables:
        problem.addVariable(name, domain)
    constr_all(problem, variables)
    return problem

def constr_all(problem, variables):
    if variables == Nil:
        return
    x = variables.head
    xs = variables.tail
    constr_between(problem, x, xs, 1)
    constr_all(problem, xs)

def constr_between(problem, x, other_variables, n):
    if other_variables == Nil:
        return
    y = other_variables.head
    ys = other_variables.tail
    no_threat(problem, x, y, n)
    constr_between(problem, x, ys, n + 1)

def no_threat(problem, x, y, j):
    problem.addConstraint(lambda x_, y_: x_ != y_ and x_ + j != y_ and x_ - j != y_, (x, y))

# demonstracni vypis
if __name__ == "__main__":
    print("CLP - Problem N dam\n")

    print("Vysledek volani queens(4).getSolutions():")
    print("------")
    for solution in queens(4).getSolutions():
        for key, value in sorted(solution.items()):
            print("%s : %s" % (key, value))
        print("------")
