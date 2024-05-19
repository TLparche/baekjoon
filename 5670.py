import sys

input = sys.stdin.readline


def insert(tree, word):
    node = tree
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    node["is_end"] = True


def check_count(tree, word):
    node = tree
    count = 1
    for i, char in enumerate(word):
        if i != 0 and len(node) > 1 or "is_end" in node:
            count += 1
        node = node[char]
    return count


while True:
    try:
        n = int(input().strip())
        words = [input().strip() for _ in range(n)]
        trie = {}
        for word in words:
            insert(trie, word)

        total_count = 0
        for word in words:
            total_count += check_count(trie, word)
        average = round(total_count / n, 2)
        print(f"{average:.2f}")
    except EOFError:
        break
    except ValueError:
        break
