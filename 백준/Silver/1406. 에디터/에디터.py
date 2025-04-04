# 1406번 에디터

import sys


left = list(sys.stdin.readline().strip())
right = []
num = int(sys.stdin.readline())

for _ in range(num):
    word = sys.stdin.readline().strip()

    if word[0] == 'L':
        if left:
            right.append(left.pop())
    elif word[0] == 'D':
        if right:
            left.append(right.pop())
    elif word[0] == 'B':
        if left:
            left.pop()
    elif word[0] == 'P':
        left.append(word[2])

print("".join(left + right[::-1]))