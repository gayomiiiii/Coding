def solution(n):
    answer = 0
    plus = []
    
    for i in range(1, n+1):
        if i%2 == 0:
            plus.append(i)
        else:
            continue
    answer = sum(plus)
    return answer