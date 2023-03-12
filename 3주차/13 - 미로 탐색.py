import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
maze = [input().rstrip() for _ in range(n)]
check = [[True] * m for _ in range(n)] # 방문 체크

cnt = []
dq = deque([[0,0,1]])
check[0][0] = False # pop하기 전에 방문체크

while dq:
    x,y,c = dq.popleft()
    if x == n-1 and y == m-1: # 도착지점에 왔으면 값 넣어주고 break
        cnt.append(c)
        break
    for a,b in [x+1, y],[x-1,y],[x,y+1],[x,y-1]: # 지점에서 4방향을 체크후에 길이 있다면 진행
        if 0 <= a < n and 0 <= b < m and maze[a][b] == '1' and check[a][b]: # 체크 사항들
            check[a][b] = False # pop하기 전에 미리 방문체크
            dq.append([a,b,c+1])

print(*cnt)

# **BFS는 방문 체크를 popleft하기 전에 해주어야 중복 체크를 막을수 있다**