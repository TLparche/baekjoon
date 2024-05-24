import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline


def tarjan_scc(v, index, lowlink, on_stack, stack, graph, scc):
    global idx
    index[v] = lowlink[v] = idx
    idx += 1
    stack.append(v)
    on_stack[v] = True
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


def check_bid(index):
    for i in range(1, n + 1):
        if index[i] == index[-i]:
            return True
    return False


n, m = map(int, input().split())
graph = [[] for _ in range(2 * n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[-a].append(b)
    graph[-b].append(a)

index = [-1] * (2 * n + 1)
lowlink = [-1] * (2 * n + 1)
on_stack = [False] * (2 * n + 1)
stack = []
scc = []
idx = 1

for i in range(1, n + 1):
    if index[i] == -1:
        tarjan_scc(i, index, lowlink, on_stack, stack, graph, scc)

scc_index = [0] * (2 * n + 1)
for i, component in enumerate(scc):
    for node in component:
        scc_index[node] = i + 1

if check_bid(scc_index):
    print(0)
else:
    print(1)
