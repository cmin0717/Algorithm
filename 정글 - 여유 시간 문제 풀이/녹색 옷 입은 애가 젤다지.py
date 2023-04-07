import sys
from heapq import *
input = sys.stdin.readline

cnt = 0 # 몇번째 입력인가 확인하기 위해
while True:
    n = int(input())
    if n == 0:break

    cave = [list(map(int,input().split())) for _ in range(n)]

    cnt += 1
    h = []
    heappush(h, [cave[0][0],0,0]) # 인자값으로 현재까지 쓴 돈과 좌표를 넣어준다.
    cave[0][0] = 'X' # 방문한곳은 X로 표시

    while h:
        cost,x,y = heappop(h)

        if x == n-1 and y == n-1: # 만일 도착지에 왔다면 출력
            print(f"Problem {cnt}: {cost}")
            break

        for i,j in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
            if 0 <= i < n and 0 <= j < n and cave[i][j] != 'X':
                heappush(h, [cost + cave[i][j],i,j])
                cave[i][j] = 'X'
