import math

def solution(a, b):
    num = math.gcd(a, b)
    b = b//num
    
    while b%2 == 0:
        b //= 2
    while b%5 == 0:
        b //= 5
    if b == 1:
        return 1
    return 2