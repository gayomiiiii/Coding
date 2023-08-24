a = input()

for i in range(len(a)):
    if a[i] != a[len(a)-i-1]:
        print("0")
        break
else:
    print("1")