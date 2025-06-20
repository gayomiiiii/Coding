n = int(input())
a_list = list(map(int, input().split()))

ans = [-1] * n   # 오큰수 결과를 담을 리스트, 처음엔 전부 -1로 초기화
stack = []       # 인덱스를 저장하는 스택

for i in range(n):
    # 현재 수가 스택에 있는 인덱스의 수보다 크면 → 오큰수 찾음
    while stack and a_list[stack[-1]] < a_list[i]:
        index = stack.pop()
        ans[index] = a_list[i]

    # 현재 인덱스를 스택에 넣음 (아직 오큰수 못 찾음)
    stack.append(i)

print(*ans)