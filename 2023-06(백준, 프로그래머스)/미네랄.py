import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
minerals = set()

for i in range(n):
    for j in range(m):
        if board[i][j] == 'x':
            minerals.add((i,j))

t = int(input())
h = list(map(int, input().split()))

def find(mineral,visit):
    q = deque([mineral])
    check = set()
    land = False

    while q:
        i,j = q.popleft()
        visit.add((i,j))
        check.add((i,j))

        if i == n-1:
            land = True

        for a,b in [i+1,j],[i-1,j],[i,j+1],[i,j-1]:
            if 0 <= a < n and 0 <= b < m and (a,b) not in visit and (a,b) in minerals:
                q.append((a,b))
    return [land, visit, check]

def cluster():
    visit = set()
    sky_cluster = set()

    for mineral in minerals:
        if mineral not in visit:
            [land, visit, check] = find(mineral, visit)
            if land == False:
                sky_cluster.update(check)
    
    return sky_cluster if sky_cluster else False

def drop(sky_cluster):
    move = float('inf')

    for x,y in sky_cluster:
        for i in range(x+1, n):
            if (i,y) in sky_cluster:
                break
            elif (i,y) in minerals:
                move = min(move, i-x-1)
                break
            elif i == n-1:
                move = min(move, i-x)
    
    for x,y in sky_cluster:
        minerals.remove((x,y))
    for x,y in sky_cluster:
        minerals.add((x+move, y))
        
for i in range(t):
    if i % 2 == 0:
        for j in range(m):
            if (n-h[i], j) in minerals:
                minerals.remove((n-h[i], j))
                break
    else:
        for j in range(m-1,-1,-1):
            if (n-h[i], j) in minerals:
                minerals.remove((n-h[i], j))
                break

    sky_cluster = cluster()
    if sky_cluster:
        drop(sky_cluster)

result = [['.']*m for _ in range(n)]
for x,y in minerals:
    result[x][y] = 'x'
for i in result:
    print(''.join(i))

# 진짜 왜 시간초과가 나오는지 모르겠다.
# 로직상 시간을 많이 잡아 먹을곳이 없는거 같은데
# 진짜 진짜 뭐가 문제인지 몰것다....