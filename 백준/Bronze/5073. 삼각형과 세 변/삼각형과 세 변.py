# 5073번 - 삼각형과 세 변

while True:
    a = sorted(list(map(int, input().split())))
    if a[0] == a[1] == a[2] == 0:
        break
    elif a[2] >= a[0] + a[1]:
        print('Invalid')
    elif a[0] == a[1] == a[2]:
        print('Equilateral')
    elif a[0] == a[1] or a[1] == a[2] or a[0]==a[2]:
        print('Isosceles')
    elif a[0] != a[1] != a[2]:
        print('Scalene')