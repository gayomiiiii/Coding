# 2798번 - 블랙잭
from itertools import combinations

n, m = map(int, input().split())
a = list(map(int, input().split()))
a_list = list(combinations(a, 3))

a_sum = [sum(a_sum) for a_sum in a_list if sum(a_sum) <= m]
print(max(a_sum))