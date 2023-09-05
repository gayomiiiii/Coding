# 2720번 - 세탁소 사장 동혁

for _ in range(int(input())):
    a = int(input())
    q, q_1 = divmod(a, 25)
    d, d_1 = divmod(q_1, 10)
    n, n_1 = divmod(d_1, 5)
    p, p_1 = divmod(n_1, 1)
    print(int(q), int(d), int(n), int(p))