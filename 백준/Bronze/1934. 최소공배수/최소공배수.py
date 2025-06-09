# 1934번 최소공배수

import math
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    gcd = math.gcd(a,b)
    print(a*b // gcd)