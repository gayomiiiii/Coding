# 1978번 소수찾기

n = int(input())
numbers = list(map(int, input().split()))
ans = []

for i in numbers:
    if i != 1:
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            ans.append(i)

print(len(ans))