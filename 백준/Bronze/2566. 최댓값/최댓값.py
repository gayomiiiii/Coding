arr = [list(map(int, input().split())) for _ in range(9)]

max_val = max(map(max, arr))
max_row, max_col = 0, 0

# 최댓값의 위치 찾기
for i in range(9):
    for j in range(9):
        if arr[i][j] == max_val:
            max_row = i+1
            max_col = j+1
            break

print(max_val)
print(max_row, max_col)