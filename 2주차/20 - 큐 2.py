import sys
from collections import deque
input = sys.stdin.readline

cnt = int(input())

result = deque()

for _ in range(cnt):
    commend = input().rstrip().split()
    if commend[0] == 'push':
        result.append(commend[1])
    elif commend[0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            pop_left = result.popleft()
            print(pop_left)
    elif commend[0] == 'size':
        print(len(result))
    elif commend[0] == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)
    elif commend[0] == 'front':
        if len(result) == 0:
            print(-1)
        else:
            print(result[0])
    else:
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])
