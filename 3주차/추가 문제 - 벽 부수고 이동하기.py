from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

maze = [input().rstrip() for _ in range(n)]
check = [[[0]*2 for _ in range(m)] for _ in range(n)] # 벽을 부순 상태와 부수지 않은 상태 2개다 표시하기 위해 3차 배열 생성

dq = deque()
dq.append([0,0,0]) # [x좌표, y좌표, 벽을 부순 상태인지 아닌지]
check[0][0][0] = 1 # 처음에는 안부순 상태이니깐 안부순 체크 박스에 체크

while dq:
    x,y,w = dq.popleft()
    if x == n-1 and y == m-1:
        print(check[x][y][w]) # 도착지점에 도착한 좌표안에 있는 cnt 출력
        break

    for a,b in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
        if 0 <= a < n and 0 <= b < m:

            if maze[a][b] == '1' and w == 0: # 처음 벽을 부순경우
                check[a][b][1] = check[x][y][0] + 1 # 벽을 부수지 않은 x,y 좌표값에 +1 해서 부순상태의 체크 박스로 넘긴다.
                dq.append([a,b,1])

            elif maze[a][b] == '0' and check[a][b][w] == 0: # 가는 곳이 벽이 아니라면 벽을 부순 상태이든 아닌 상태든 
                check[a][b][w] = check[x][y][w] + 1         # 각자의 체크 박스에 +1 해주고 저장
                dq.append([a,b,w])
else:
    print(-1)

# 3차 배열을 이용한 문제이다. 3차 배열 사용할 생각도 자주 해야할듯하다.
# 벽을 부순 상태로 움직이는 방문 체크와 안부수고 가는 방문 체크를 따로 해준다.
# 2차 배열을 2개 만들어서 해도 될듯하다. 해보지는 않음ㅎ