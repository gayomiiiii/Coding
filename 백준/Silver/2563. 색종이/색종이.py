matrix = [[0 for i in range(100)] for j in range(100)]
# matrix = [[0]*100 for _ in range(100)]
count = 0

a = int(input())

for i in range(a):
    x, y = map(int, input().split())
    
    for i in range(x, x+10):
        for j in range(y, y+10):
            matrix[i][j] = 1
        
for i in matrix:
    count += i.count(1)
print(count)