import sys

input = sys.stdin.readline


def failure(string_list):
    string_len = len(string_list)
    F = [0 for _ in range(string_len)]
    j = 0
    for i in range(1, string_len):
        while j > 0 and string_list[i] != string_list[j]:
            j = F[j - 1]
        if string_list[i] == string_list[j]:
            j += 1
            F[i] = j
    return F


l = int(input().strip())
ad_str = list(input().strip())
F = failure(ad_str)
result = l - F[l - 1]
print(result)
