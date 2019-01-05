#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from __future__ import division
from linked_lists import LinkedList, Cons, Nil
from best_search import BestSearch

biggest = 99
start = (LinkedList([("t1", 4), ("t2", 2), ("t3", 2), ("t4", 20),
                     ("t5", 20), ("t6", 11), ("t7", 11)]),
         LinkedList([("idle", 0), ("idle", 0), ("idle", 0)]), 0)

precedence = dict(
    t1=["t4", "t5"],
    t2=["t4", "t5"],
    t3=["t5", "t6", "t7"])

def goes_before(T1, T2):
    if T1 in precedence:
        if T2 in precedence[T1]:
            return True
        for T in precedence[T1]:
            if goes_before(T, T2):
                return True
    return False

def is_goal(state):
    # zavisi na resenem problemu
    waiting, _, _ = state
    return waiting == Nil

def move_anyYC(state):
    # zavisi na resenem problemu
    tasks1, active, fin1 = state
    _, f = active.head
    active1 = active.tail
    for (task, d), tasks2 in del1_anyX(tasks1):
        permissible = True
        for t, _ in member_anyX(tasks2):
            if goes_before(t, task):
                permissible = False
        for t1, f1 in member_anyX(active1):
            if f < f1 and goes_before(t1, task):
                permissible = False
        if not permissible:
            continue
        active2, fin2 = insert((task, f+d), active1, fin1)
        cost = fin2 - fin1
        yield ((tasks2, active2, fin2), cost)
    for active3 in insert_idle(f, active1):
        yield ((tasks1, active3, fin1), 0)

def insert(task, active, f1):
    s, a = task
    if active == Nil:
        return (Cons((s, a), Nil), a)
    t, b = active.head
    l = active.tail
    if a <= b:
        return (Cons((s, a), active), f1)
    l1, f2 = insert((s, a), l, f1)
    return (Cons((t, b), l1), f2)

def insert_idle(a, active):
    if active == Nil:
        return
    t, b = active.head
    l = active.tail
    if a < b:
        yield Cons(("idle", b), active)
    else:
        for l1 in insert_idle(a, l):
            yield Cons((t, b), l1)

def h(state):
    waiting, active, fin = state
    waiting_time = 0
    for _, execution_time in waiting:
        waiting_time = waiting_time + execution_time
    active_time = 0
    cpu_number = 0
    for _, finishing_time in active:
        active_time = active_time + finishing_time
        cpu_number = cpu_number + 1
    finall = (waiting_time + active_time) / cpu_number
    return max(finall - fin, 0)

def del1_anyX(ys):
    if ys == Nil:
        return
    yield (ys.head, ys.tail)
    for (z, zs) in del1_anyX(ys.tail):
        yield (z, Cons(ys.head, zs))

def member_anyX(xs):
    if xs == Nil:
        return
    yield xs.head
    for x in member_anyX(xs.tail):
        yield x

def writelist(xs):
    writelist_(xs, 1)

def writelist_(xs, i):
    if xs != Nil:
        print("%d: %s" % (i, xs.head))
        writelist_(xs.tail, i+1)

# demonstracni vypis
if __name__ == "__main__":
    print("Rozvrh prace procesoru, algoritmus A*\n")
    print("Pocatecni stav: %s" % (start,))

    print("\nNalezene reseni:")
    astar = BestSearch(biggest, is_goal, move_anyYC, h)
    solution = next(astar.search(start))
    print("Prohledano %d stavu, vysledne reseni ma cenu %d." % (astar.total, solution.head[2]))
    writelist(solution.reverse())
