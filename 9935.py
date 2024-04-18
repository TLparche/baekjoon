import sys

string = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
len_bomb = len(bomb)
result = []
for char in string:
    result.append(char)
    if len(result) >= len_bomb and ''.join(result[-len_bomb:]) == bomb:
        del result[-len_bomb:]
if len(result) == 0:
    sys.stdout.write("FRULA")
else:
    sys.stdout.write("".join(result))
