# 9012번 괄호
a = int(input())

for i in range(a):
    s = input()
    ans = []

    for j in s:
        if j == '(':
            ans.append(j)
        else:
            if ans:
                ans.pop()
            else:
                ans.append(')')
                break
    print('YES' if not ans else 'NO')