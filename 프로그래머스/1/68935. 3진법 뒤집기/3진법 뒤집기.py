def solution(n):
    base = ''
    while n > 0:
        n, b = divmod(n, 3)
        base += str(b)
    return int(base, 3)