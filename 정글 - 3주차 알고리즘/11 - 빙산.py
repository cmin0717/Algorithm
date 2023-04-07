from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(n)] # 남극 지도 저장

def bfs(arr):
    dq = deque() 
    dq.append(arr)

    while dq:
        i,j = dq.popleft()
        cnt = 0
        for a,b in [i+1,j],[i-1,j],[i,j+1],[i,j-1]: # pop한 좌표에 상하좌우를 조건을 체크한 후 조건에 맞으면 큐에 넣어 다시 진행
            if 0 <= a < n and 0 <= b < m and maps[a][b] != 0:
                cnt += 1 # 상하좌우에 빙하의 개수를 cnt변수에 담아준다.
                if check[a][b] == False: # 방문했으니 방문 체크
                    check[a][b] = True
                    dq.append([a,b])
        li.append([i,j,4-cnt]) # 빙하가 물에 잠기는걸 나중에 한꺼번에 해주어야하기에 li리스트에 담아준다.

year = 0
while True:
    check = [[False]*m for _ in range(n)] # 매번 방문 체크를 해주어야하기에 while문 시작에 만들어준다.
    li = []
    count = 0 # 빙하가 연결되어 있는지 확인하기위해 count변수 생성

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 0 and check[i][j] == False:
                check[i][j] = True
                bfs([i,j]) # bfs를 1번했는데 다시 bfs를 진행한다는 말은 빙하가 한덩어리 구성되지 않았다는 말이다.
                count += 1

    if count > 1: # 카운트가 1 이상이면 빙하가 1개 이상의 덩어리로 구성 되어있는것
        print(year)
        break

    if li:
        for x,y,c in li:
            if maps[x][y] - c > 0:
                maps[x][y] -= c
            else:
                maps[x][y] = 0
        year += 1
    else: # li가 비어있다는건 잠길 빙하가 없다는 말
        print(0)
        break
 



