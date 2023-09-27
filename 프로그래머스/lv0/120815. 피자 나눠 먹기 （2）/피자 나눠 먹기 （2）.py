def solution(n):
    # answer = 0
    if n % 6 == 0:
        answer = n//6
    else:
        for i in range(1, n+1):
            if 6*i % n == 0:
                answer = i
                break
            else:
                i += 1
    return answer