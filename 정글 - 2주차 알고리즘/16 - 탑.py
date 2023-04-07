import sys
input = sys.stdin.readline


n = int(input())

tower = list(map(int,input().split()))

stack = []
receiver = []

for i in range(n):
    while stack:
        if stack[-1][1] > tower[i]: # stack[-1][1]이 더 크다면 송신할수있다는 말이므로
            receiver.append(stack[-1][0] + 1) # 인덱스에 표시
            break
        else:
            stack.pop() # 타워가 stack보다 크다면 지우고 현재 타워를 넣는다. stack보다 크다는건 앞쪽에 수신해줄 높이의 수신기가 없다는것이다.
    if not stack: # 스텍에 없다면 송신할 높이의 수신기가 없기에 0추가
        receiver.append(0)
    stack.append([i,tower[i]]) # 타워가 크든 작든 일단 stack 넣어준다.

print(*receiver)


# 시간 초과난 코드....
# receiver = [0] * n
# cnt = n-1

# while len(tower) > 1:
#     check = tower.pop()
#     for i in range(len(tower)-1,-1,-1):
#         if tower[i] > check:
#             receiver[cnt] = i+1
#             cnt -= 1
#             break
#     else:
#         cnt -= 1

# print(*receiver)