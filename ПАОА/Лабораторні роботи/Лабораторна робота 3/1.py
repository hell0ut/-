#!/bin/python3
import math
import os


def bfs(n, m, edges, start_node):
    edge_weight = 6
    weights = [-1] * (n-1)
    return _inner_bfs(n, m, edges, start_node, edge_weight, None, weights)


def _inner_bfs(n, m, edges, start_node, distance, active_nodes, weights_list):
    next_step_nodes = []

    if active_nodes is None:
        active_nodes = [start_node]

    if len(active_nodes) == 0:
        return weights_list

    for node in active_nodes:
        for edge in edges:

            new_node = None
            if edge[0] == node:
                new_node = edge[1]

            if edge[1] == node:
                new_node = edge[0]

            if new_node and new_node != start_node:
                if new_node < start_node:
                    i = new_node - 1
                else:
                    i = new_node - 2

                if weights_list[i] > distance or weights_list[i] == -1:
                    weights_list[i] = distance
                    next_step_nodes.append(new_node)

    return _inner_bfs(n, m, edges, start_node, distance + 6, next_step_nodes, weights_list)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
