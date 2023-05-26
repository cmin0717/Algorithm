from copy import deepcopy
from collections import deque
from heapq import *

def solution(land, h):
    n,m = len(land), len(land[0])
    arr = deepcopy(land)
    part = []
    
    # 각 소속을 찾아준다.
    def find(x,y):
        q = deque([[x,y]])
        p = set()
        while q:
            i,j = q.popleft()
            if (i,j) in p:
                continue
            p.add((i,j))
            for a,b in [i+1,j],[i-1,j],[i,j+1],[i,j-1]:
                if 0 <= a < n and 0 <= b < m and abs(land[i][j] - land[a][b]) <= h:
                    q.append([a,b])
            arr[i][j] = 'a'
        part.append(list(p))
        
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 'a':
                find(i,j)
    
    # 각 위치가 어디 소속인지 표시
    for i in range(len(part)):
        for j in part[i]:
            land[j[0]][j[1]] = [land[j[0]][j[1]], i]
    
    # 보드를 다 돌면선 다른소속으로 가는 값이 가장 작은것만 기록한다.
    dic = {}
    for x in range(n):
        for y in range(m):
            for a,b in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
                if 0 <= a < n and 0 <= b < m and abs(land[x][y][0] - land[a][b][0]) > h and land[x][y][1] != land[a][b][1]:
                    key = (min(land[x][y][1],land[a][b][1]), max(land[x][y][1],land[a][b][1]))
                    dic.setdefault(key, float('inf'))
                    dic[key] = min(dic[key], abs(land[x][y][0] - land[a][b][0]))

    # 위에서 얻은 각 소속끼리의 간선 정보를 가지고 최소신장트리 구함             
    link = [[] for _ in range(len(part))]
    for k,v in dic.items():
        link[k[0]].append([v, k[1]])
        link[k[1]].append([v, k[0]])
    
    h, visit = [[0,0]], [0]*len(part)
    result = 0
    while h:
        cost, idx = heappop(h)
        if visit[idx] != 0:
            continue
        visit[idx] = 1
        result += cost
        for i in link[idx]:
            if visit[i[1]] == 0:
                heappush(h, i)
    return result
    