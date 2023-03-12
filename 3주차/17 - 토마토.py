from collections import deque # heapq를 사용하다가 시간초과나서 생각해보니깐 heapq을 사용할 필요가 없었다.
import sys
input = sys.stdin.readline

row,col,h = map(int,input().split())

tomato = [list(map(int,input().split())) for _ in range(col * h)]

dq = deque()

for i in range(col*h): # 3차원 배열을 2차원으로 저장하기 위해 세로 * 높이만큼 세로를 잡았다. 
    for j in range(row):
        if tomato[i][j] == 1: # 익은 사과가 있는 좌표를 미리 dq에 넣어준다.
            dq.append([0,i,j]) # [지난 일수,x좌표,y좌표]

result = 0
while dq:
    day,x,y = dq.popleft()
    result = max(day,result) # 값을 가져올때마다 지난 일수 변환환

    for a,b in [x+1,y],[x-1,y],[x,y+1],[x,y-1]: # 같은 층에있는 상하좌우
        if col*(x//col) <= a < col*(x//col+1) and 0 <= b < row and tomato[a][b] == 0: # 2차배열로 표시했기에 a좌표를 값을 특정해서 정해주어야한다.
            tomato[a][b] = day+1
            dq.append([day+1,a,b])

    for a,b in [x+col,y],[x-col,y]: # 위 아래 상자를 확인한다.
        if 0 <= a < col * h and 0 <= b < row and tomato[a][b] == 0:
            tomato[a][b] = day + 1
            dq.append([day+1,a,b])

for i in range(col * h):
    if 0 in set(tomato[i]): # 익지 않은 사과를 체크 있다면 -1출력
        print(-1)
        break
else:
    print(result)
