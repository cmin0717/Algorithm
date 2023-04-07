from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

shark = 2
sea = []
st = []

def check(x,y,i,j): # 해당 좌표 물고기 까지의 최소 거리 구하는 함수
    dq = deque()
    m = [[0] * n for _ in range(n)]
    m[x][y] = 1
    dq.append([0,x,y])
    while dq:
        f = dq.popleft()
        if f[1] == i and f[2] == j:
            return f[0]
        for a,b in [f[1]+1, f[2]],[f[1], f[2]-1],[f[1], f[2]+1],[f[1]-1, f[2]]:
            if 0 <= a < n and 0 <= b < n and sea[a][b] <= shark and m[a][b] == 0:
                dq.append([f[0]+1,a,b])
                m[a][b] = 1
    else:
        return 0

def find_food(x,y):
    # 거리 1인 인접 물고기 확인 위 좌 우 하 순서로 확인
    for i,j in [x-1, y],[x, y-1],[x, y+1],[x+1, y]:
        if 0 <= i < n and 0 <= j < n and sea[i][j] < shark and sea[i][j] != 0:
            return [[1,i,j]]

    food = []
    # 먹을 수 있는 물고기 체크
    for i in range(n):
        for j in range(n):
            if sea[i][j] != 0 and sea[i][j] < shark:
                d = check(x,y,i,j)
                if d != 0:
                    food.append([d,i,j])
    food.sort(key=lambda x : (x[0],x[1],x[2])) # 거리가 제일 짧고 상 좌로 정렬

    if len(food) == 0:
        return []
    else:
        return [food[0]]

for i in range(n):
    m = list(map(int, input().split()))
    sea.append(m)
    if 9 in set(m):
        idx = [i, m.index(9)]
sea[idx[0]][idx[1]] = 0
st = find_food(idx[0], idx[1])

time = 0
growth = 0
while st:
    fish = st[0]
    time += fish[0]
    growth += 1
    if growth == shark:
        shark += 1
        growth = 0
    x = fish[1]
    y = fish[2]
    sea[x][y] = 0
    st = find_food(x,y)
print(time)