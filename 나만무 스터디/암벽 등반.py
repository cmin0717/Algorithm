import sys
from collections import deque
input = sys.stdin.readline

n,t = map(int,input().split())

furrows = set()

for _ in range(n): # set자료형에 넣기위해 튜플 사용
    x,y = map(int,input().split())
    furrows.add((x,y))

q = deque([])
q.append([0,0,0]) # x,y값과 cnt 초기값 넣어줌

while q:
    x,y,cnt = q.popleft()
    
    if y == t: # 정상에 도착했으면 현재 cnt 출력
        print(cnt)
        break

    for i in range(x-2,x+3): # 각 범위를 구해서 해당 좌표에 홈이 있나 확인
        for j in range(y-2,y+3):
            if (i,j) in furrows: # 있다면 큐에 넣고 해당 홈을 삭제
                q.append([i,j,cnt+1])
                furrows.remove((i,j))
else:
    print(-1)




