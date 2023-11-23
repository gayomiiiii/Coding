# ATM - 11399번

a = input()
time_li = list(map(int, input().split()))
time = []
t = 0

time_li.sort()
for i in time_li:
    t += i
    time.append(t)
print(sum(time))