import sys
from collections import deque
input = sys.stdin.readline

n, p, k = map(int,input().split())
link = [[] for _ in range(n+1)]
start, end = 0, 0

for _ in range(p):
    s,e,c = map(int, input().split())
    link[s].append([e,c])
    link[e].append([s,c])
    end = max(0, c)
temp = end

# 다익스트라를 이용하여 무료로 받을수 있는 전선를 기준으로 최대값 추출
def check(mid):
    q = deque([[0, 1]])
    dist = [float('inf')] * (n+1)
    dist[1] = 0

    while q:
        cost, idx = q.popleft()

        if dist[idx] < cost:
            continue

        for i,c in link[idx]:
            d = cost
            if c > mid:
                d += 1
            if d < dist[i]:
                q.append([d, i])
                dist[i] = d
    
    return dist[n] <= k

while start < end:
    mid = (start + end) // 2
    if check(mid):
        end = mid
    else:
        start = mid + 1

if end == temp:
    print(-1)
else:
    print(end)
