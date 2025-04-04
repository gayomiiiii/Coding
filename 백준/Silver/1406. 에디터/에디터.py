import sys

left_stack = list(sys.stdin.readline().strip())  # 초기 문자열을 왼쪽 스택에 저장
right_stack = []

M = int(sys.stdin.readline().strip())  # 명령어 개수

for _ in range(M):
    cmd = sys.stdin.readline().strip().split()
    
    if cmd[0] == 'L':  
        if left_stack:
            right_stack.append(left_stack.pop())
    
    elif cmd[0] == 'D':  
        if right_stack:
            left_stack.append(right_stack.pop())
    
    elif cmd[0] == 'B':  
        if left_stack:
            left_stack.pop()
    
    elif cmd[0] == 'P':  
        left_stack.append(cmd[1])  

# 결과 출력
print("".join(left_stack + right_stack[::-1]))