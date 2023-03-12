import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
paper = [list(map(int,input().split())) for _ in range(n)]
count = 0
max_size = 0

def find(i,j): # bfs를 통해 해당 그림의 크기를 알아오고 0으로 바꾸어준다.
    global count, max_size
    q = deque([[i,j]])
    paper[i][j] = 0
    count += 1
    size = 0
    while q:
        x,y = q.popleft()
        size += 1
        for a,b in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
            if 0 <= a < n and 0 <= b < m and paper[a][b] == 1:
                paper[a][b] = 0
                q.append([a,b])
    else:
        max_size = max(max_size, size)

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            find(i,j)
print(count, max_size, sep='\n')