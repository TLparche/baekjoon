import sys

sentence_a = " " + sys.stdin.readline().strip()
sentence_b = " " + sys.stdin.readline().strip()
dp = [[0 for _ in range(len(sentence_b))] for _ in range(len(sentence_a))]
for i in range(1, len(sentence_a)):
    for j in range(1, len(sentence_b)):
        if sentence_a[i] == sentence_b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])
