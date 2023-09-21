"""
Six brothers are eating together at a circular table, numbered 1 through 6. Brothers with numbers
that are one apart don't get along and don't want to sit next to each other.
Additionally, brothers 3 and 5 also do not get along.
Sit them at the circular table so they can all eat peacefully.
"""

from collections import defaultdict


def add_edge(graph, a, b):
    graph[a].add(b)
    graph[b].add(a)


def all_pairs(nodes):
    for i, a in enumerate(nodes):
        for b in nodes[i+1:]:
            yield a, b


def invert_graph(graph):
    inverse = defaultdict(set)
    nodes = sorted(graph.keys())
    for (a, b) in all_pairs(nodes):
        if a != b and a not in graph[b]:
            add_edge(inverse, a, b)
    return inverse


def find_hamiltonian_cycle(graph):
    start = next(iter(graph))
    path = [start]
    if search(graph, start, path):
        return path


def search(graph, node, path):
    if len(path) == len(graph):
        # Return if current node links to start node
        return path[0] in graph[node]

    for neighbor in graph[node]:
        if neighbor not in path:
            path.append(neighbor)
            if search(graph, neighbor, path):
                return path
            path.pop()

    return False


if __name__ == '__main__':
    disagreements = defaultdict(set)
    add_edge(disagreements, 1, 2)
    add_edge(disagreements, 2, 3)
    add_edge(disagreements, 3, 4)
    add_edge(disagreements, 4, 5)
    add_edge(disagreements, 5, 6)
    add_edge(disagreements, 3, 5)
    agreements = invert_graph(disagreements)
    arrangement = find_hamiltonian_cycle(agreements)
    print(arrangement)
