# 3009번 - 네 번째 점
x_num = []
y_num = []

for i in range(3):
    a, b = map(int,input().split())
    x_num.append(a)
    y_num.append(b)

for i in range(3):
    if x_num.count(x_num[i]) == 1:
        x = x_num[i]
    if y_num.count(y_num[i]) == 1:
        y = y_num[i]
        
print(x, y)