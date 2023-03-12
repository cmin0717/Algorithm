import sys
input = sys.stdin.readline

# Kruskal MST 알고리즘
# union-find 알고리즘

v,e = map(int,input().split())
peak = [i for i in range(v+1)] # 각자 부모로 있는 노드를 만들어준다.

line = [list(map(int,input().split())) for _ in range(e)]
line.sort(key=lambda x: x[2]) # 간선 비용을 기준으로 오름차순 정렬한다. 제일 작은값부터 넣어야하기 떄문에

def find(x):
    if peak[x] != x: # 자기 자신이 부모가 아니라면 자기 자신을 부모로 가진 수를 재귀로 찾는다.
        peak[x] = find(peak[x])
    return peak[x]

def union(x,y):
    a = find(x)
    b = find(y)
    if a < b:
        peak[b] = a # 더 큰 부모를 가진쪽 부모의 값을 작은 부모의 값으로 바꾼다.
        # for i in range(1,v+1): 
        #     if peak[i] == b:   
        #         peak[i] = a    
    else:
        peak[a] = b
        # for i in range(1,v+1): # 굳이 for문으로 다 안바꾸어도 되는게 어차피 find에서 부모의 값을 가져오는거니깐
        #     if peak[i] == a:   # 부모의 값만 바꾸어주면 된다.
        #         peak[i] = b    # find가 없었다면 for문을 통해 이렇게 다바꾸어 주어야할듯하다
    return

cnt = 0
for x,y,cost in line:
    if find(x) != find(y): # 부모의 값이 다르면 사이클에 겹치지 않기 때문에 진행해도 된다.
        union(x,y) # x,y가 연결되었으니깐 같은 부모에 넣어준다.
        cnt += cost

print(cnt)

# prim 알고리즘

from heapq import *

v,e = map(int,input().split())
node = [[] for _ in range(v+1)] # 연결 리스트를 받을 공간

for _ in range(e):
    x,y,z = map(int,input().split())
    node[x].append([z,y]) # 간선의 가중치를 앞쪽에 넣어준다. 이따 힙으로 가장 작은 것부터 빼기 위해
    node[y].append([z,x])

check = [0] * (v + 1)
hq = [[0,1]] # 1부터 시작 , 자기 자신으로 가는건 값이 없으니깐 0을 넣어준다.
cnt = 0

while hq:
    a,b = heappop(hq)
    if check[b] == 0: # 방문 하지 않았다면 진행
        check[b] = 1 # 방문 체크
        cnt += a # 가중치 더해주고
        for i,j in node[b]: # 새로 연결된 노드와 연결된 방문하지 않은 노드들 힙에 추가
            if check[j] == 0:
                heappush(hq,[i,j])
print(cnt)
