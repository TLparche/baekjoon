import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def tarjan_scc(v, index, lowlink, on_stack, stack, graph, scc):
    global idx
    index[v] = lowlink[v] = idx
    idx += 1
    stack.append(v)
    on_stack[v] = True
    if v in graph:
        for w in graph[v]:
            if index[w] == -1:
                tarjan_scc(w, index, lowlink, on_stack, stack, graph, scc)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], index[w])

    if lowlink[v] == index[v]:
        component = []
        while True:
            w = stack.pop()
            on_stack[w] = False
            component.append(w)
            if w == v:
                break
        scc.append(sorted(component))


def scc_indegree(scc, graph):
    scc_index = {}
    for i, component in enumerate(scc):
        for node in component:
            scc_index[node] = i

    indegree = [0] * len(scc)

    for u in range(v):
        if u in graph:
            for w in graph[u]:
                if scc_index[u] != scc_index[w]:
                    indegree[scc_index[w]] += 1

    return indegree


for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)

    index = [-1] * v
    lowlink = [-1] * v
    on_stack = [False] * v
    stack = []
    scc = []
    idx = 1

    for i in range(v):
        if index[i] == -1:
            tarjan_scc(i, index, lowlink, on_stack, stack, graph, scc)

    indegree = scc_indegree(scc, graph)

    if indegree.count(0) == 1:
        for i in scc[indegree.index(0)]:
            print(i)
    else:
        print("Confused")
    _ = input()
    print()
