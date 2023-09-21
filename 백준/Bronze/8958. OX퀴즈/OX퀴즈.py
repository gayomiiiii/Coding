n = int(input())

for i in range(n):
    quiz = list(input())
    sum = 0
    quiz_sum = 0
    for j in quiz:
        if j == 'O':
            sum += 1
            quiz_sum += sum
        else:
            sum = 0
    print(quiz_sum)