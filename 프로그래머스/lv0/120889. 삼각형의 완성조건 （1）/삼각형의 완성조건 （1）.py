def solution(sides):
    s = sorted(sides)
    if s[2] < s[0] + s[1]:
        return 1
    else:
        return 2