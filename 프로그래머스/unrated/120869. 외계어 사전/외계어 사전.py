from itertools import permutations

def solution(spell, dic):
    answer = 0
    a = list("".join(p) for p in permutations(spell, len(spell)))
    for i in a:
        if i in dic:
            answer = 1
            break
        else:
            answer = 2
    return answer