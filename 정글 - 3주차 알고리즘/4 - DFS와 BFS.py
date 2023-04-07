import sys
from collections import deque

input = sys.stdin.readline

n,m,v = map(int,input().split())

li = [[] for _ in range(n+1)]
result_dfs = []
result_bfs = []

for _ in range(m):
    x,y = map(int,input().split())
    li[x].append(y)
    li[y].append(x)

for i in range(n+1): # 쌍방향이므로 정렬시켜도 문제 없다.
    if len(li[i]) > 1:
        li[i].sort()

def dfs(x): # 깊이 우선 탐색
    if x not in set(result_dfs): # 연결된게 벌써 갔다온곳이 아니라면
        result_dfs.append(x) 
        for i in li[x]:
            if i not in set(result_dfs): # 연결된곳에 다시 재귀로 들어간다.
                dfs(i)
    return

def bfs(x): # 너비 우선 탐색
    check = deque()
    check.append(x)
    result_bfs.append(x)
    while check: # 큐로 앞에서 부터 하나씩 꺼내서 확인
        node = check.popleft()
        for i in li[node]:
            if i not in result_bfs: # 갔던곳이 아니라면
                result_bfs.append(i) # 값을 미리 넣어주고 연결된곳은 큐 뒤에 넣어 나중에 확인
                check.append(i)
dfs(v)
bfs(v)
print(*result_dfs)
print(*result_bfs)


