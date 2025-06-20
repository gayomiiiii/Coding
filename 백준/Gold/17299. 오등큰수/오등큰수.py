
from collections import Counter

n = int(input())
a_list = list(map(int, input().split()))

ans = [-1] * n   
freq = Counter(a_list)  
stack = []    


for i in range(n):
    while stack and freq[a_list[stack[-1]]] < freq[a_list[i]]:
        index = stack.pop()
        ans[index] = a_list[i]

    stack.append(i)

print(*ans)
