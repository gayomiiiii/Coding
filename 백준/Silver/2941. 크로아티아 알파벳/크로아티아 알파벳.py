word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()

for i in word:
    a = a.replace(i, '*')

print(len(a))