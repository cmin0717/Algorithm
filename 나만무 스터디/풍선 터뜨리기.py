import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
ballon = list(map(int,input().split()))
ballons = [[ballon[i], i+1] for i in range(n)]

q = deque(ballons)

result = []

while q:
    info = q.popleft()
    result.append(info[1])
    if info[0] > 0:
        q.rotate(1 - info[0])
    else:
        q.rotate(-(info[0]))

print(*result)
