import sys
from collections import deque
input = sys.stdin.readline

n,k,r = map(int, input().split())

form = set()
cows = []

# 목초지 사이의 길을 set자료형에 저장
for _ in range(r):
    x,y,x1,y1 = map(int, input().split())
    form.add((x,y,x1,y1))
    form.add((x1,y1,x,y))

# 소들의 좌표 저장
for _ in range(k):
    x,y = map(int, input().split())
    cows.append([x,y])

# 소 이동
def move(x,y,idx):
    q = deque([[x,y]])
    visit = [[True] * (n+1) for _ in range(n+1)]
    visit[x][y] = False

    while q:
        i,j = q.popleft()

        for a,b in [i+1,j],[i-1,j],[i,j+1],[i,j-1]:
            if 0 < a <= n and 0 < b <= n:
                # 방문한적 없는 목초지이면서 현재 목초지와 길을 건너지 않아도 갈수있는 목초지만 보낸다.
                if visit[a][b] and (i,j,a,b) not in form:
                    visit[a][b] = False
                    q.append([a,b])

    # 길을 건너지 않고 갈수있는 곳은 다 확인했음으로 소의 위치에 해당하는 곳을 갈수없다면 +1해준다.
    cnt = 0
    for x,y in cows[idx+1:]:
        if visit[x][y]:
            cnt += 1
    return cnt

# 소들을 앞에서부터 완탐
result = 0
for i in range(k):
    x,y = cows[i]
    result += move(x, y, i)

print(result)