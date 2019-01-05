#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

from __future__ import division
import math
from linked_lists import LinkedList, Cons, Nil

# prevod z faktu na parametry
def induce():
    examples = get_examples()
    attributes = get_attribute_names()
    return induce_tree(attributes, examples)

def induce_tree(attributes, examples):
    if examples == Nil:
        return None
    example = examples.head
    class_, _ = example
    other_class = False
    for example1 in member_anyX(examples):
        classX, _ = example1
        if classX != class_:
            other_class = True
            break
    if other_class is False:
        # priklady stejne klasifikace
        return ("leaf", class_)
    attribute, _ = choose_attribute(attributes, examples)
    if attribute is None:
        # zadny uzitecny atribut, list s distribuci klasifikaci
        exclasses = get_example_classes(examples)
        return ("leaf", exclasses)
    rest_atts = del_(attribute, attributes)
    values = get_attribute_values(attribute)
    subtrees = induce_trees(attribute, values, rest_atts, examples)
    return ("tree", attribute, subtrees)

def induce_trees(att, vals, rest_atts, exs):
    if vals is Nil:
        # no attributes, no subtrees
        return Nil
    val1 = vals.head
    example_subset = attval_subset(att, val1, exs)
    tree1 = induce_tree(rest_atts, example_subset)
    trees = induce_trees(att, vals.tail, rest_atts, exs)
    return Cons((val1, tree1), trees)

def attval_subset(attribute, value, examples):
    return filter_examples(examples, None, attribute, value)

def choose_attribute(atts, examples):
    if atts == Nil:
        return (None, 0)
    att = atts.head
    if atts.tail == Nil:
        gain_ = gain(examples, att)
        return (att, gain_)
    best_att1, best_gain1 = choose_attribute(atts.tail, examples)
    gain_ = gain(examples, att)
    if gain_ > best_gain1:
        return (att, gain_)
    return (best_att1, best_gain1)

def gain(exs, att):
    att_vals = get_attribute_values(att)
    total = length(exs)
    classes = get_example_classes(exs)
    ccnts = cnt_classes(classes, exs)
    i = info(ccnts, total)
    rem_ = rem(att, att_vals, exs, classes, total)
    gain_ = i - rem_
    return gain_

def info(value_counts, total):
    if value_counts == Nil:
        return 0
    vc = value_counts.head
    i1 = info(value_counts.tail, total)
    if vc == 0:
        return i1
    pvi = vc / total
    return -pvi * math.log(pvi, 2) + i1

def rem(att, vs, exs, classes, total):
    if vs == Nil:
        return 0
    v = vs.head
    nv = length(filter_examples(exs, None, att, v))
    vcnts = cnt_classes_attv(att, v, classes, exs)
    pv = nv / total
    i = info(vcnts, nv)
    rem1 = rem(att, vs.tail, exs, classes, total)
    return pv * i + rem1

def cnt_classes(classes, exs):
    if classes == Nil:
        return Nil
    c = classes.head
    nc = cnt_class(c, exs)
    ncs = cnt_classes(classes.tail, exs)
    return Cons(nc, ncs)

def cnt_class(class_, exs):
    count = 0
    for example in member_anyX(exs):
        class1, _ = example
        if class1 == class_:
            count = count + 1
    return count

def cnt_classes_attv(att, val, classes, exs):
    if classes == Nil:
        return Nil
    c = classes.head
    nc = cnt_class_attv(att, val, c, exs)
    ncs = cnt_classes_attv(att, val, classes.tail, exs)
    return Cons(nc, ncs)

def cnt_class_attv(att, val, class_, exs):
    return length(filter_examples(exs, class_, att, val))

def get_example_classes(examples):
    if examples == Nil:
        return Nil
    example = examples.head
    class_, _ = example
    other_classes = get_example_classes(examples.tail)
    if not member(class_, other_classes):
        return Cons(class_, other_classes)
    return other_classes

# filtruj priklady podle hodnoty atributu a volitelne i podle tridy vystupu
def filter_examples(examples, class_, attribute, value):
    if examples == Nil:
        return Nil
    example = examples.head
    class1, obj = example
    other_examples = filter_examples(examples.tail, class_, attribute, value)
    if class_ is None or class_ == class1:
        if member((attribute, value), obj):
            return Cons(example, other_examples)
    return other_examples

def member(x, ys):
    if ys == Nil:
        return False
    if x == ys.head:
        return True
    return member(x, ys.tail)

def member_anyX(xs):
    if xs == Nil:
        return
    yield xs.head
    for x in member_anyX(xs.tail):
        yield x

def length(xs):
    if xs == Nil:
        return 0
    return 1 + length(xs.tail)

def del_(x, ys):
    if ys == Nil:
        return Nil
    if x == ys.head:
        return ys.tail
    return Cons(ys.head, del_(x, ys.tail))

example_list = LinkedList([
    ("pockat", LinkedList([
        ("alt", "ano"), ("bar", "ne"), ("paso", "ne"), ("hlad", "ano"),
        ("stam", "cast"), ("cen", "$$$"), ("dest", "ne"), ("rez", "ano"),
        ("typ", "mexicka")
    ])),
    ("necekat", LinkedList([
        ("alt", "ano"), ("bar", "ne"), ("paso", "ne"), ("hlad", "ano"),
        ("stam", "plno"), ("cen", "$"), ("dest", "ne"), ("rez", "ne"),
        ("typ", "asijska")
    ])),
    ("pockat", LinkedList([
        ("alt", "ne"), ("bar", "ano"), ("paso", "ne"), ("hlad", "ne"),
        ("stam", "cast"), ("cen", "$"), ("dest", "ne"), ("rez", "ne"),
        ("typ", "bufet")
    ])),
    ("pockat", LinkedList([
        ("alt", "ano"), ("bar", "ne"), ("paso", "ano"), ("hlad", "ano"),
        ("stam", "plno"), ("cen", "$"), ("dest", "ne"), ("rez", "ne"),
        ("typ", "asijska")
    ])),
    ("necekat", LinkedList([
        ("alt", "ano"), ("bar", "ne"), ("paso", "ano"), ("hlad", "ne"),
        ("stam", "plno"), ("cen", "$$$"), ("dest", "ne"), ("rez", "ano"),
        ("typ", "mexicka")
    ])),
    ("pockat", LinkedList([
        ("alt", "ne"), ("bar", "ano"), ("paso", "ne"), ("hlad", "ano"),
        ("stam", "cast"), ("cen", "$$"), ("dest", "ano"), ("rez", "ano"),
        ("typ", "pizzerie")
    ])),
    ("necekat", LinkedList([
        ("alt", "ne"), ("bar", "ano"), ("paso", "ne"), ("hlad", "ne"),
        ("stam", "nikdo"), ("cen", "$"), ("dest", "ano"), ("rez", "ne"),
        ("typ", "bufet")
    ])),
    ("pockat", LinkedList([
        ("alt", "ne"), ("bar", "ne"), ("paso", "ne"), ("hlad", "ano"),
        ("stam", "cast"), ("cen", "$$"), ("dest", "ano"), ("rez", "ano"),
        ("typ", "asijska")
    ])),
    ("necekat", LinkedList([
        ("alt", "ne"), ("bar", "ano"), ("paso", "ano"), ("hlad", "ne"),
        ("stam", "plno"), ("cen", "$"), ("dest", "ano"), ("rez", "ne"),
        ("typ", "bufet")
    ])),
    ("necekat", LinkedList([
        ("alt", "ano"), ("bar", "ano"), ("paso", "ano"), ("hlad", "ano"),
        ("stam", "plno"), ("cen", "$$$"), ("dest", "ne"), ("rez", "ano"),
        ("typ", "pizzerie")
    ])),
    ("necekat", LinkedList([
        ("alt", "ne"), ("bar", "ne"), ("paso", "ne"), ("hlad", "ne"),
        ("stam", "nikdo"), ("cen", "$"), ("dest", "ne"), ("rez", "ne"),
        ("typ", "asijska")
    ])),
    ("pockat", LinkedList([
        ("alt", "ano"), ("bar", "ano"), ("paso", "ano"), ("hlad", "ano"),
        ("stam", "plno"), ("cen", "$"), ("dest", "ne"), ("rez", "ne"),
        ("typ", "bufet")
    ]))])

attribute_dict = dict(
    bar=LinkedList(["ano", "ne"]),
    paso=LinkedList(["ano", "ne"]),
    hlad=LinkedList(["ano", "ne"]),
    stam=LinkedList(["nikdo", "cast", "plno"]),
    cen=LinkedList(["$", "$$", "$$$"]),
    dest=LinkedList(["ano", "ne"]),
    rez=LinkedList(["ano", "ne"]),
    typ=LinkedList(["mexicka", "asijska", "bufet", "pizzerie"]))
attribute_list = LinkedList(["bar", "paso", "hlad", "stam", "cen", "dest", "rez", "typ"])

def get_examples():
    # zavisi na resenem problemu
    return example_list

def get_attribute_names():
    # zavisi na resenem problemu
    return attribute_list

def get_attribute_values(attribute):
    # zavisi na resenem problemu
    return attribute_dict[attribute]

# demonstracni vypis
if __name__ == "__main__":
    print(induce())
