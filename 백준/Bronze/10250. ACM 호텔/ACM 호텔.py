# 10250 - ACM 호텔
a = int(input())

for _ in range(a):
    room = []
    h, w, n = map(int, input().split())
    for i in range(1, w+1):
        for j in range(1, h+1):
            r = (str(j)+str(format(i, '02')))
            room.append(r)
    print(room[n-1])