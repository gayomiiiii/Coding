# 1676번 0의 개수

n = int(input())

ans = 1
for i in range(2, n+1):
    ans *= i

answer = 0
for j in str(ans)[::-1]:
    if j == '0':
        answer += 1
        pass
    else:
        break
print(answer)