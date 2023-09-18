n = int(input())

for i in range(1, n+1):
    n_sum = sum(map(int, str(i)))
    n_sum += i
    if n_sum == n:
        print(i)
        break
else:
    print(0)