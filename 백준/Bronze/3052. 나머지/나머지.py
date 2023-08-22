# 3052 - 나머지

result = []

for i in range(10):
    data = int(input())
    result.append (data % 42)
    
result = set(result)
result = list(result)
print(len(result))
    