# 10828번 스택

import sys
n = int(sys.stdin.readline())
stack = []

for i in range(n):
    ans = sys.stdin.readline().split()
    if ans[0] == 'push':
        stack.append(ans[1])
    elif ans[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif ans[0] == 'size':
        print(len(stack))
    elif ans[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])