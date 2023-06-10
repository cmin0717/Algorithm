import sys
from collections import deque
input = sys.stdin.readline

n,q = map(int, input().split())

usado = [list(map(int, input().split())) for _ in range(n-1)]
quest = [list(map(int, input().split())) for _ in range(q)]

link = [[] for _ in range(n+1)]
for s,e,c in usado:
    link[s].append([e,c])
    link[e].append([s,c])

def create(v):
    dq = deque()
    dist = [float('inf')] * (n+1)
    visit = [False] * (n+1)

    for i in link[v]:
        dq.append(i)
        dist[i[0]] = i[1]

    while dq:
        idx, cost = dq.popleft()

        if visit[idx]: continue
        visit[idx] = True

        for info in link[idx]:
            new_cost = min(cost, info[1])
            # 아직 방문한적 없고 유사도가 높은경우만 추가
            if dist[info[0]] > new_cost and not visit[info[0]]:
                dist[info[0]] = new_cost
                dq.append([info[0], new_cost])
    
    # 해당 비디오와 각 비디오의 최적의 유사도를 구하고 리턴
    return dist[1:]


dic = {}
for k,v in quest:
    # 해당 동영상의 유사도를 처음 구한다면 구하고 저장
    if dic.get(v) == None:
        dic[v] = create(v)
    
    cnt = 0
    for i in range(n):
        if i+1 == v: continue
        if dic[v][i] >= k:
            cnt += 1
    print(cnt)