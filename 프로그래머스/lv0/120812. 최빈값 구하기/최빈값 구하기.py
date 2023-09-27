def solution(array):
    answer = 0
    ary = list(set(array))
    cnt = []
    for i in ary:
        cnt.append(array.count(i))
        if cnt.count(max(cnt)) > 1:
            answer = -1
        else:
            answer = ary[cnt.index(max(cnt))]
    return answer