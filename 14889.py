import sys


def dfs(depth, player):
    global gap
    if depth == n // 2:
        opposite = list(set(i for i in range(n)) - set(player))
        team_score_a, team_score_b = 0, 0
        for i in player:
            for j in player:
                team_score_a += table[i][j]
        for i in opposite:
            for j in opposite:
                team_score_b += table[i][j]
        gap = min(gap, abs(team_score_a - team_score_b))
        return

    for i in range(player[-1] + 1, n):
        player.append(i)
        dfs(depth + 1, player)
        player.pop()


n = int(sys.stdin.readline().strip())
table = [[] * n] * n
gap = float("inf")
for i in range(n):
    table[i] = list(map(int, sys.stdin.readline().strip().split()))
for i in range(n // 2):
    player_fi = [i]
    dfs(1, player_fi)
print(gap)
