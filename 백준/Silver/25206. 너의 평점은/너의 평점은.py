# 25206번 - 너의 평점은
final = 0
total = 0

grade_score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']

for i in range(20):
    a, b, c = input().split()
    b = float(b)
    if c != 'P':
        total += b
        final += b * grade_score[grade.index(c)]
print('{:.6f}'.format(final/total))