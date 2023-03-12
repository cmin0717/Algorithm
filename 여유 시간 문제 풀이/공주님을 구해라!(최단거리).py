import sys
from collections import deque
input = sys.stdin.readline

n,m,t = map(int,input().split())
castle = [list(map(int,input().split())) for _ in range(n)]
check = [[0] * m for _ in range(n)]

q = deque([])
q.append([0,0,0])
check[0][0] = 1
result = float('inf')

while q:
    x,y,time = q.popleft()
    
    if x == n-1 and y == m-1: # 하나라도 공주에 도착하면 종료
        result = min(result, time)
        break

    if time > t: continue # 현재 시간이 주어진 시간보다 같거나 크면 패쓰

    if castle[x][y] == 2: # 검을 찾았고 일직선으로 공주한테 가는 시간이 주어진 시간보다 적으면 갱신
        newtime = time+(n-x-1)+(m-1-y)
        if newtime <= t:
            result = min(result, newtime)

    for i,j in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
        if 0 <= i < n and 0 <= j < m and check[i][j] == 0:
            if castle[i][j] == 2 or castle[i][j] == 0:
                check[i][j] = 1
                q.append([i,j,time+1])

if result == float('inf'): # 값이 갱신되지 못했다면 못구했으니 Fail출력
    print("Fail") # 대소문자 잘 구별하자
else:
    print(result)



