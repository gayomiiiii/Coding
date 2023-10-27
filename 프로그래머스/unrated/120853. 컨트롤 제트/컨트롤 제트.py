def solution(s):
    answer = 0
    answer_li = s.split()
    for i in range(len(answer_li)):
        if answer_li[i] == 'Z':
            answer -= int(answer_li[i-1])
        else:
            answer += int(answer_li[i])
    return answer