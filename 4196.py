import sys

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
                if lowlink[w] <= index[v]:
                    indegree[w] -= 1
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                if lowlink[w] <= index[v]:
                    indegree[w] -= 1
                lowlink[v] = min(lowlink[v], index[w])

    if lowlink[v] == index[v]:
        component = []
        ssc_indegree.append(0)
        while True:
            w = stack.pop()
            on_stack[w] = False
            component.append(w)
            ssc_indegree[-1] += indegree[w]
            if w == v:
                break
        scc.append(sorted(component))


for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = {}
    indegree = [0] * (v + 1)
    for _ in range(e):
        a, b = map(int, input().split())
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        indegree[b] += 1

    index = [-1] * (v + 1)
    lowlink = [-1] * (v + 1)
    on_stack = [False] * (v + 1)
    stack = []
    scc = []
    idx = 1
    ssc_indegree = []

    for i in range(1, v + 1):
        if index[i] == -1:
            tarjan_scc(i, index, lowlink, on_stack, stack, graph, scc)

    print(ssc_indegree.count(0))
