#!/usr/bin/env python
# encoding=utf-8 (pep 0263)

""" Graf rumunskych mest vcetne predpocitanych vzdalenosti
    mezi mesty a predpocitanou vzdusnou vzdalenosti do Bukuresti """

graph = dict(
    Arad=([
        ("Sibiu", 140),
        ("Timisoara", 118),
        ("Zerind", 75),
    ], 366),
    Bukurest=([
        ("Fagaras", 211),
        ("Giurgiu", 90),
        ("Pitesti", 101),
        ("Urziceni", 85),
    ], 0),
    Craiova=([
        ("Dobreta", 120),
        ("Pitesti", 138),
        ("Rimnicu_Vilcea", 146),
    ], 160),
    Dobreta=([
        ("Craiova", 120),
        ("Mehadia", 75),
    ], 242),
    Fagaras=([
        ("Bukurest", 211),
        ("Sibiu", 99),
    ], 178),
    Eforie=([
        ("Hirsova", 86),
    ], 161),
    Giurgiu=([
        ("Bukurest", 90),
    ], 77),
    Hirsova=([
        ("Eforie", 86),
        ("Urziceni", 98),
    ], 151),
    Iasi=([
        ("Neamt", 87),
        ("Vaslui", 92),
    ], 226),
    Lugoj=([
        ("Mehadia", 70),
        ("Timisoara", 111),
    ], 244),
    Mehadia=([
        ("Dobreta", 75),
        ("Lugoj", 70),
    ], 241),
    Neamt=([
        ("Iasi", 87),
    ], 234),
    Oradea=([
        ("Sibiu", 151),
        ("Zerind", 71),
    ], 380),
    Pitesti=([
        ("Bukurest", 101),
        ("Craiova", 138),
        ("Rimnicu_Vilcea", 87),
    ], 98),
    Rimnicu_Vilcea=([
        ("Craiova", 146),
        ("Pitesti", 97),
        ("Sibiu", 80),
    ], 193),
    Sibiu=([
        ("Arad", 140),
        ("Fagaras", 99),
        ("Oradea", 151),
        ("Rimnicu_Vilcea", 80),
    ], 253),
    Timisoara=([
        ("Arad", 118),
        ("Lugoj", 111),
    ], 320),
    Urziceni=([
        ("Bukurest", 85),
        ("Hirsova", 98),
        ("Vaslui", 142),
    ], 80),
    Vaslui=([
        ("Iasi", 92),
        ("Urziceni", 142),
    ], 199),
    Zerind=([
        ("Arad", 75),
        ("Oradea", 71),
    ], 374))
