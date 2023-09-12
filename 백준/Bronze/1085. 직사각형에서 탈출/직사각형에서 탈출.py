a,b,c,d = map(int, input().split())

print(min(d-b, c-a, b-0, a-0))