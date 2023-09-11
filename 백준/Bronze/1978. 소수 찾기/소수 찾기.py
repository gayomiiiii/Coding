# 1978번 - 소수 찾기

n = int(input())
a = list(map(int, input().split()))
cnt = []

for i in a:
    if i != 1:
        is_prime_flag = True
        for j in range(2, i):
            if i % j == 0:
                is_prime_flag = False
                break
        if is_prime_flag:
            if i not in cnt:
                cnt.append(i)


print(len(cnt))