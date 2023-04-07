from collections import deque
import sys
input = sys.stdin.readline

s,t = map(int,input().split()) # 시작값과 도착값을 받는다.

dq = deque([[s, ''],[1, '/']]) # 초기값으로 시작값과 /를 한번 한 [1, '/']를 넣어준다.
result = []
check = float('inf') # 초기값을 맥스값으로 설정

while dq:
    info = dq.popleft()
    num = info[0]
    operator = info[1]
    if len(operator) > check:continue # check값 보다 높다면 확인할 필요가 없다.

    if num == t:
        l_o = len(operator)
        if l_o < check:
            result = []
            check = l_o
        if l_o != 0:
            result.append(operator)

    if num**2 <= t and num != 1:
        dq.append([num**2, operator + '*'])
    if num*2 <= t :
        dq.append([num*2, operator + '+'])

if len(result) != 0: # 조건에 따라 결과를 출력
    print(sorted(result)[0])
elif s == t:
    print(0)
else:
    print(-1)
