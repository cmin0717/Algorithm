import sys
sys.setrecursionlimit(10**6) # 재귀의 깊이를 설정해줘야 통과한다.
input = sys.stdin.readline

# dfs 풀이법
n = int(input())
node = [[] for _ in range(n+1)] # 각 노드의 연결리스트
peak = [list(map(int,input().split())) for _ in range(n-1)]
result = [0] * (n+1)  # 각 노드의 부모값을 저장할 공간

for x,y in peak:
    node[x].append(y)
    node[y].append(x)

def check(x,y):
    if x == 1:
        result[x] = 1 # 입력받은 값이 1이면 루트이기에 그냥 1입력
    else:
        result[x] = y # 1이 아닐경우에는 함수 호출시 넣어주었던 값이 부모의 값이다.
    for i in node[x]:
        if result[i] == 0: # 부모의값이 0이라면 아직 부모가 없기에 진행할수있다.
            check(i,x) # 다음으로 알아볼 i와 i의 부모값인 x를 같이 넣어준다.
check(1,0)

for i in result[2:]: # 2부터 필요하니깐 나머지는 스킵
    print(i)

# -----------------------------------------------------------------------------------------------------------------
# bfs 풀이법 - 메모리적으로 더 좋았음 시간은 거의 비슷
from collections import deque 

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(x):
    dq = deque([x]) # 1부터 시작하여 위에서 아래로 부모의 값을 찾아 넣는다.

    while dq:
        m = dq.popleft() 
        for i in graph[m]:
            if parents[i] == 0 and i != 1:
                dq.append(i)
                parents[i] = m


parents = [0] * (n+1)
bfs(1)
print(*parents[2:],sep='\n')