# 14215번 - 세 막대

s = sorted(list(map(int, input().split())))

if s[0] + s[1] > s[2]:
    print(sum(s))
else:
    print(2*(s[0]+s[1])-1)