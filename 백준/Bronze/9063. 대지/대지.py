n = int(input())
a=[]
b=[]

if n == 1:
    print('0')
else:
    for _ in range(n):
        c, d = map(int, input().split())
        a.append(c)
        b.append(d)
    print((max(a)- min(a))*(max(b)-min(b)))