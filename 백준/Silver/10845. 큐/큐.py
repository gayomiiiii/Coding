# 10845번 큐

import sys

n = int(sys.stdin.readline())
ans = []

for _ in range(n):
    word = sys.stdin.readline().strip().split()

    if word[0] == 'push':
        ans.append(word[1])
    elif word[0] == 'pop':
        if ans:
            print(ans.pop(0))
        else:
            print(-1)
    elif word[0] == 'empty':
        print(0 if ans else 1)
    elif word[0] == 'size':
        print(len(ans))
    elif word[0] =='front':
        print(ans[0] if ans else -1)
    elif word[0] == 'back':
        print(ans[-1] if ans else -1)