def solution(n):
    answer = []
    for i in range(1, n+1):
        if n%i == 0:
            answer.append(i)
        else:
            continue
    return sorted(answer, reverse=False)