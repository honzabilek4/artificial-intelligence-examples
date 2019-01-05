#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

import heapq
from linked_lists import LinkedList, Cons, Nil

# horni zavora pro cenu nejlepsi cesty
biggest = 9999

# Algoritmus funguje analogicky k algoritmu ze souboru
# 4.1_9-priority-queue.py, ale namisto jednotlivych uzlu udrzujeme ve
# fronte skupiny uzlu, ze kterych je nutne se dostat do koncovych uzlu
# pro splneni vsech jiz navstivenych AND uzlu. Na zaver jsou cesty
# jednotlivych uzlu zrekonstruovany do stromu.
def andor(start):
    heap = [(0, 0, LinkedList([(0, 0, 0, start, Nil)]), Nil)]
    while True:
        try:
            f, g, nodes, solved = heapq.heappop(heap)
        except IndexError: # fronta je prazdna
            raise ValueError("Reseni neexistuje.")
        if nodes == Nil: # seznam uzlu k vyreseni je prazdny
            return reconstruct_search_tree(solved)
        _, g1, c, node, path = nodes.head
        if is_goal(node):
            solved = Cons((node, Cons(node, path)), solved)
            heapq.heappush(heap, (f-h(node)-c, g-c, nodes.tail, solved))
        elif f <= biggest:
            succ = get_successors(node)
            if succ is None: # narazili jsme na necilovy uzel
                continue
            op, successors = succ
            path1 = Cons(node, path)
            if op == "and":
                nodes1 = nodes.tail
                for m, c in successors:
                    if not member(m, path1):
                        nodes1 = insert((g1+c+h(m), g1+c, c, m, path1), nodes1)
                        f = g + c + h(m)
                        g = g + c
                heapq.heappush(heap, (f, g, nodes1, solved))
            if op == "or":
                for m, c in successors:
                    if not member(m, path1):
                        nodes1 = insert((g1+c+h(m), g1+c, c, m, path1), nodes.tail)
                        heapq.heappush(heap, (g+c+h(m), g+c, nodes1, solved))

def reconstruct_search_tree(leaves):
    tree = dict()
    for node, path in leaves:
        tree[node] = "goal"
        while path != Nil and path.tail != Nil:
            node = path.head
            parent = path.tail.head
            if parent not in tree:
                op, _ = get_successors(parent)
                tree[parent] = (op + "_result", LinkedList([node]))
            else:
                op, nodes = tree[parent]
                if not member(node, nodes):
                    tree[parent] = (op, Cons(node, nodes))
                break
            path = path.tail
    return tree

def insert(node, nodes):
    if nodes == Nil:
        return LinkedList([node])
    f = node[0]
    f1 = nodes.head[0]
    if f <= f1:
        return Cons(node, nodes)
    return Cons(nodes.head, insert(node, nodes.tail))

def member(x, xs):
    if xs == Nil:
        return False
    if x == xs.head:
        return True
    return member(x, xs.tail)

def h(_):
    # zavisi na resenem problemu
    return 0

graph = dict(
    a=("or", LinkedList([("b", 1), ("c", 3)])),
    b=("and", LinkedList([("d", 1), ("e", 1)])),
    c=("and", LinkedList([("f", 2), ("g", 1)])),
    e=("or", LinkedList([("h", 6)])),
    f=("or", LinkedList([("h", 2), ("i", 3)])))

goals = dict(d=True, g=True, h=True)

def is_goal(node):
    # zavisi na resenem problemu
    return node in goals

# tato funkce nahrazuje prologovska fakta tvaru node ---> Op:Subtrees
# a pro zadany node navraci prislusne Op:Subtrees
def get_successors(node):
    # zavisi na resenem problemu
    if node in graph:
        return graph[node]
    return None

# demonstracni vypis
if __name__ == "__main__":
    print('Prohledavani AND/OR grafu - implementace pomoci prioritni fronty')
    print('\n  Graf:')
    print('    a ---> or:[b/1,c/3].')
    print('    b ---> and:[d/1,e/1].')
    print('    c ---> and:[f/2,g/1].')
    print('    e ---> or:[h/6].')
    print('    f ---> or:[h/2,i/3].')
    print('    h(X,0).')
    print('    goal(d).')
    print('    goal(g).')
    print('    goal(h).')
    print('\nVysledky dotazu andor("a"):')
    solution = andor("a")
    for key, value in sorted(solution.items()):
        print("%s : %s" % (key, value))
