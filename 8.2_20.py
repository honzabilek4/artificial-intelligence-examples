#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from linked_lists import LinkedList, Cons, Nil

def preposition_symbols(_):
    # zavisi na resenem problemu
    return LinkedList(["p1", "p2", "p3"])

def pl_true(formula, model):
    # zavisi na resenem problemu
    if formula == "kb":
        return model == LinkedList([("p3", True), ("p2", True), ("p1", True)]) or \
               model == LinkedList([("p3", True), ("p2", True), ("p1", False)])
    if formula == "alpha":
        return model == LinkedList([("p3", True), ("p2", True), ("p1", True)]) or \
               model == LinkedList([("p3", False), ("p2", True), ("p1", True)]) or \
               model == LinkedList([("p3", True), ("p2", True), ("p1", False)]) or \
               model == LinkedList([("p3", False), ("p2", True), ("p1", False)])
    if formula == "beta":
        return model == LinkedList([("p3", True), ("p2", True), ("p1", True)]) or \
               model == LinkedList([("p3", True), ("p2", False), ("p1", True)]) or \
               model == LinkedList([("p3", False), ("p2", True), ("p1", True)]) or \
               model == LinkedList([("p3", False), ("p2", False), ("p1", True)])

def tt_entails(kb, alpha):
    symbols = preposition_symbols(LinkedList([kb, alpha]))
    return tt_check_all(kb, alpha, symbols, Nil)

def tt_check_all(kb, alpha, symbols, model):
    if symbols == Nil:
        if pl_true(kb, model):
            return pl_true(alpha, model)
        return True
    p = symbols.head
    return tt_check_all(kb, alpha, symbols.tail, Cons((p, True), model)) and \
           tt_check_all(kb, alpha, symbols.tail, Cons((p, False), model))

# demonstracni vypis
if __name__ == "__main__":
    print("KB entails Alpha: %s" % tt_entails("kb", "alpha"))
    print("KB entails Beta: %s" % tt_entails("kb", "beta"))
