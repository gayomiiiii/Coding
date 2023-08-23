a = input()
b = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS','TUV', 'WXYZ']
result = 0

for i in range(len(a)):
    for j in b:
        if a[i] in j:
            result += b.index(j)+3
print(result)