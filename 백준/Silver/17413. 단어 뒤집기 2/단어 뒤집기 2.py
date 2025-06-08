s = input()
stack = []
in_tag = False

for char in s:
    if char == '<':
        # 단어를 뒤집고 태그 여는 기호 출력
        while stack:
            print(stack.pop(), end='')
        in_tag = True
        print('<', end='')
    elif char == '>':
        in_tag = False
        print('>', end='')
    elif in_tag:
        # 태그 안이면 그냥 출력
        print(char, end='')
    elif char == ' ':
        # 단어 끝났을 때 뒤집고 공백 출력
        while stack:
            print(stack.pop(), end='')
        print(' ', end='')
    else:
        # 평범한 문자면 스택에 쌓음
        stack.append(char)

# 마지막에 남은 단어 뒤집어서 출력
while stack:
    print(stack.pop(), end='')
