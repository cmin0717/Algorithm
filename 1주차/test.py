from heapq import * 
import sys
input = sys.stdin.readline

n = int(input())

maze = [input().rstrip() for _ in range(n)]
dis = [[float('inf')]*n for _ in range(n)]

dis[0][0] = 0
hq = []
heappush(hq,[0,0,0])

while hq:
    cost,x,y = heappop(hq)

    if dis[x][y] < cost:
        continue
    for a,b in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
        if 0 <= a < n and 0 <= b < n and dis[a][b] > cost:
            if maze[a][b] == '0':
                dis[a][b] = cost + 1
                heappush(hq, [cost+1,a,b])
            else:
                dis[a][b] = cost
                heappush(hq, [cost,a,b])
print(dis[n-1][n-1])