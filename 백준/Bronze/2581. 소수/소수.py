# 2581번 - 소수

m = int(input())
n = int(input())

cnt = []

for i in range(m, n+1):
    if i != 1:
        is_prime_flag = True
        for j in range(2, i):
            if i % j == 0:
                is_prime_flag = False
                break
        if is_prime_flag:
            if i not in cnt:
                cnt.append(i)

if cnt:
    print(sum(cnt))
    print(min(cnt))
else:
    print('-1')