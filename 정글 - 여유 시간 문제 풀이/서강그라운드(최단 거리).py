import sys
from heapq import *
input = sys.stdin.readline

n,m,r = map(int,input().split())
items = list(map(int,input().split()))
link = [[] for _ in range(n+1)]

for _ in range(r): # 입력 받은 정보를 연결리스트에 담아둔다.
    x,y,c = map(int,input().split())
    link[x].append([y,c])
    link[y].append([x,c])

def check(start): # 다익스트라 알고리즘으로 각 출발점에서 각 지점까지의 최단거리를 구한다.
    h = []
    heappush(h, [0, start])
    dist[start] = 0

    while h:
        dis, idx = heappop(h)

        if dist[idx] < dis: # 만일 현재 거리정보에 있는 거리길이가 더 최단이면 패쓰한다.
            continue

        for info in link[idx]:
            new_dist = info[1] + dist[idx]
            if new_dist < dist[info[0]]:
                dist[info[0]] = new_dist
                heappush(h, [new_dist, info[0]])

result = 0

for i in range(1,n+1): # 각 출발점마다 최단거리를 구한다
    dist = [float('inf')] * (n+1)
    count = 0
    check(i)
    for j in range(1,n+1): # 지점마다의 거리가 m보다 작으면 아이템을 먹을수 있으니 count변수에 더해준다.
        if dist[j] <= m:
            count += items[j-1]
    result = max(result, count) # 각 출발점마다 먹을수 있는 아이템개수의 최대값을 result변수에 저장
print(result)

