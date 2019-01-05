#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import Cons, Nil    

def solution(n=8):
    if n == 0:
        yield Nil
    else:
        for others in solution(n-1):
            for x in range(1, 9):
                for y in range(1, 9):                    
                    if noattack(x, y, others):
                        yield Cons((x, y), others)

def noattack(x, y, others):
    if others == Nil:
        return True
    else:
        x1, y1 = others.head
        return x != x1 and y != y1 and y1-y != x1-x and y1-y != x-x1 and \
               noattack(x, y, others.tail)

# demonstracni vypis
if __name__ == "__main__":    
    print("PROBLEM OSMI DAM I")
    print("Volani next(solution()) : %s" % next(solution(8)))    
