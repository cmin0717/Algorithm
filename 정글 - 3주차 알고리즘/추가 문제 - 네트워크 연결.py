import sys
input = sys.stdin.readline

# kruskal 풀이법
n = int(input())
m = int(input())

parents = [i for i in range(n+1)]
network = [list(map(int,input().split())) for _ in range(m)]
network.sort(key=lambda x :x[2]) # 가중치를 기준으로 오름차순으로 만들어준다.

def find(x): # x의 부모가 누군지 찾는 함수
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x,y): # x,y의 부모를 하나로 통일 시키는 함수
    a = find(x)
    b = find(y)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

result = 0
for x,y,cost in network: # 부모 노드가 다른 간선의 가중치가 작은것 부터 하나씩 가져와서 비용을 완성 시킨다.
    if find(x) != find(y):
        union(x,y)
        result += cost
print(result)


# prim 풀이

from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

li = [[] for _ in range(n+1)] # 양방향으로 연결리스트를 작성
check = [0] * (n+1) # 방문 체크

for _ in range(m):
    x,y,z = map(int,input().split())
    li[x].append([z,y])
    li[y].append([z,x])

hq = []
heappush(hq,[0,1]) # 시작점을 넣어준다. 아무거나 넣어도 상관 없다.

cnt = 0
while hq:
    cost,idx = heappop(hq) # hq에서 가중치가 작은것 부터 가져온다.
    if check[idx] == 0:
        check[idx] = 1 # 방문체크 해주고
        cnt += cost
        for c,x in li[idx]:
            if check[x] == 0:
                heappush(hq,[c,x])
print(cnt)

