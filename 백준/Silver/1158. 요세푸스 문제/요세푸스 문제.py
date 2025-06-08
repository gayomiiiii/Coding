# 1158번 요세푸스 문제
from collections import deque

a, b = map(int, input().split())

que = deque(range(1, a+1))
ans = [] 

while que:
    for _ in range(b-1):
        que.append(que.popleft())
    ans.append(que.popleft())

print("<" + ', '.join(map(str, ans)) + ">")