from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
maze = [input().rstrip() for _ in range(n)]
check = [[float('inf')] * n for _ in range(n)] # 각 위치를 일단 최대값으로 설정

hq = []
heappush(hq,[0,0,0]) # 시작점이 왼쪽 위 방부터 시작하니깐 0,0,0을 넣어준다.[현재까지오기까지 검은방을 바꾼횟수,x좌표,y좌표]
check[0][0] = 0 # 시작점은 항상 흰방이니깐 0으로 설정

while hq:
    c,x,y = heappop(hq) # 방을  가장 적게 바꾼 횟수부터 heapq으로 뺀다.

    for a,b in [x+1,y],[x-1,y],[x,y+1],[x,y-1]: # 현재 위치에서 4방향으로 좌표를 준다.
        if 0 <= a < n and 0 <= b < n and check[a][b] > c: # 해당 좌표가 올바른 인덱스이고 
            if maze[a][b] == '0':                         # 여기까지 올때까지 방을 바꾼횟수가 전에 있던 방을 바꾼횟수보다 적을경우 작업 진행
                check[a][b] = c+1 # 검은 방이면 c에 +1해주고
                heappush(hq, [c+1,a,b]) # 새로운 c를 넣어준다.
            else:
                check[a][b] = c
                heappush(hq, [c,a,b]) # 흰방이면 받은 그대로 좌표만 바꾸어 전달

print(check[n-1][n-1])
