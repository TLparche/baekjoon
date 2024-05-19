import sys

input = sys.stdin.readline


def insert(tree, word):
    node = tree
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    node["is_end"] = True


def print_tire(tree, depth):
    for char in tree:
        if char == "is_end":
            continue
        print("--" * depth, end="")
        print(char)
        print_tire(tree[char], depth + 1)


trie = {}
infos = []
N = int(input())
for _ in range(N):
    infos.append(input().split()[1:])
infos.sort()

for info in infos:
    insert(trie, info)
print_tire(trie, 0)
