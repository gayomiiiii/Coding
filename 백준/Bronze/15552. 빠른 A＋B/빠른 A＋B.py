import sys
r = int(input())

for i in range(r):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)