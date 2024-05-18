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


def kmp(fir_str, sec_str):
    match_count = [0 for _ in range(len(fir_str))]
    count = 0
    index = []
    F = failure(sec_str)
    j = 0
    for i in range(len(fir_str)):
        while j > 0 and fir_str[i] != sec_str[j]:
            j = F[j - 1]
        if fir_str[i] == sec_str[j]:
            j += 1
            match_count[i] = j

        if match_count[i] == len(sec_str):
            index.append(i - len(sec_str) + 2)
            count += 1
            j = F[-1]
    return count, index


T = list(input())
P = list(input())

count, index = kmp(T, P)
print(count)
print(*index)
