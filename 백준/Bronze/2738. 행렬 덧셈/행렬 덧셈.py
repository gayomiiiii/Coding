# 2738번 - 행렬 덧셈
n, m = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)] 

def plus(arr1, arr2):
    for j in range(len(arr1)):
        for k in range(len(arr1[j])):
            arr1[j][k] = arr1[j][k]+arr2[j][k]
    return arr1

arr = plus(arr1, arr2)
for row in arr:
    print(*row)