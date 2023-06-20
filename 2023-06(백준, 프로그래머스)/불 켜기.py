import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
link = [[[] for _ in range(n+1)] for _ in range(n+1)]
bright = [[False] * (n+1) for _ in range(n+1)]
visit = set()

# 주어진 정보로 링크를 만든다.
for _ in range(m):
    x,y,x1,y1 = map(int, input().split())
    link[x][y].append([x1,y1])

# 불을 켠 방을 갈수있다면 true 없다면 false 리턴(주어진 방의 네방향중 하나라도 방문을 했다면 갈수있다.)
def check(x,y):
    for i,j in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
        if (i,j) in visit:
            return True
    return False

q = deque([[1,1]])
bright[1][1] =  True
count = 1

while q:
    x,y = q.popleft()

    # 해당 방에서 불을 켤수있는 방을 모두 킨다.
    for i,j in link[x][y]:
        if not bright[i][j]:
            bright[i][j] = True
            count += 1
            # 불 킨방을 갈수있다면 큐에 추가 후 방문 처리
            if check(i,j):
                q.append([i,j])
                visit.add((i,j))
                
    # 해당 위치에서 네방향중 불이 켜져있고 방문하지 않았다면 방문
    for i,j in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
        if 0 < i <= n and 0 < j <= n and bright[i][j] and (i,j) not in visit:
            visit.add((i,j))
            q.append([i,j])
print(count)