import sys
from heapq import *
input = sys.stdin.readline

n, start = map(int, input().split())
link = [[] for _ in range(n)]

for i in range(n):
    dist = list(map(int, input().split()))
    for j in range(n):
        if i == j: continue
        link[i].append([dist[j], j])

h = [[0, start, 2**start]]
check = {}
result = 0

while h:
    tt, now, visit = heappop(h)

    # 비트 마스킹을 이용하여 모두 한번씩은 갔다왔다면 현재까지 tt값을 출력
    if visit == 2**(n) - 1:
        print(tt)
        break

    for cost,next in link[now]:
        # 딕셔너리에 현재 방문 리스트와 다음 방문지를 현재 tt값 기준으로 저장
        if (visit, next) in check:
            # 현재 tt값보다 작은값으로 간적이 있다면 PASS
            if check[(visit, next)] <= tt+cost:
                continue
        check[(visit, next)] = tt+cost
        heappush(h, [tt+cost, next, visit | 2**next])