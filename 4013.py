import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


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
    new_graph = defaultdict(list)
    for u in range(1, v + 1):
        if u in graph:
            for w in graph[u]:
                if scc_index[u] != scc_index[w]:
                    new_graph[scc_index[u]].append(scc_index[w])
                    indegree[scc_index[w]] += 1

    return new_graph, indegree


def topological_sort(graph, indegree):
    zero_indegree_queue = deque([i for i in range(len(indegree)) if indegree[i] == 0])
    top_order = []

    while zero_indegree_queue:
        node = zero_indegree_queue.popleft()
        top_order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                zero_indegree_queue.append(neighbor)

    return top_order


def find_max_money(new_graph, top_order, start_scc, new_money, restaurant_sccs):
    dp = [-1] * len(new_graph)
    dp[start_scc] = new_money[start_scc]

    for node in top_order:
        if dp[node] == -1:
            continue
        for neighbor in new_graph[node]:
            dp[neighbor] = max(dp[neighbor], dp[node] + new_money[neighbor])

    return max(dp[r] for r in restaurant_sccs)


v, e = map(int, input().split())
graph = defaultdict(list)
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

index = [-1] * (v + 1)
lowlink = [-1] * (v + 1)
on_stack = [False] * (v + 1)
stack = []
scc = []
idx = 1

money = [0] * (v + 1)
for i in range(1, v + 1):
    money[i] = int(input())

start, p = map(int, input().split())
restaurant = list(map(int, input().split()))

for i in range(1, v + 1):
    if index[i] == -1:
        tarjan_scc(i, index, lowlink, on_stack, stack, graph, scc)

new_money = [0] * len(scc)
scc_index = {}
for i, component in enumerate(scc):
    for node in component:
        scc_index[node] = i
        new_money[i] += money[node]

new_graph, indegree = scc_indegree(scc, graph)
top_order = topological_sort(new_graph, indegree)

start_scc = scc_index[start]
restaurant_sccs = list(map(lambda x: scc_index[x], restaurant))

result = find_max_money(new_graph, top_order, start_scc, new_money, restaurant_sccs)

print(result)
