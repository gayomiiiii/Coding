# 보물 - 1026번

n = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = 0
a.sort(reverse=True)
b.sort()

for i, j in zip(a, b):
    answer += i*j
print(answer)