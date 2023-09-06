a, b = map(int, input().split())
num = []
for i in range(1, a+1):
    if a % i == 0:
        num.append(i)
if len(num) < b:
    print('0')
else:
    print(num[b-1])