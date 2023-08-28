num = int(input())
a = num

for i in range(num):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            continue
        elif word[j] in word[j+1:]:
            a -= 1
            break
print(a)