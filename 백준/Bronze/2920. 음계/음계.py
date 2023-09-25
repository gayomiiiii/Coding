# 2920번 - 음계

a = list(map(int, input().split()))

if sorted(a) == a:
    print('ascending')
elif sorted(a, reverse = True) == a:
    print('descending')
else:
    print('mixed')