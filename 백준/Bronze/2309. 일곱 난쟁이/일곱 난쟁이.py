# 일곱 난쟁이 - 2309번

from itertools import combinations

answer = []
nine = []
for i in range(9):
    n = int(input())
    nine.append(n)

all = [list(map(int, combination)) for combination in combinations(nine, 7)]

for i in all:
    if sum(i) == 100:
        answer.append(i)
        break

answer[0].sort()
for i in answer[0]:
    print(i)