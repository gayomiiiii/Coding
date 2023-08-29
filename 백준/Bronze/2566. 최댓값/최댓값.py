arr = [list(map(int, input().split())) for _ in range(9)]

max_val = max(map(max, arr))
max_list = [(i+1,j+1) for i in range(9) for j in range(9) if arr[i][j] == max_val]
print(max_val)

for row in max_list:
    print(*row)