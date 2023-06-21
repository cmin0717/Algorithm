import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
minerals = set()

# 미네랄의 좌표를 set으로 저장한다.
for i in range(n):
    for j in range(m):
        if board[i][j] == 'x':
            minerals.add((i,j))

t = int(input())
h = list(map(int, input().split()))

# 각각의 미네랄이 떨어지는것인지 붙어있는것인지 판단
def find(mineral,visit):
    q = deque([mineral])
    check = set()
    visit.add((mineral[0], mineral[1]))
    check.add((mineral[0], mineral[1]))
    land = False

    while q:
        i,j = q.popleft()

        if i == n-1:
            land = True

        for a,b in [i+1,j],[i-1,j],[i,j+1],[i,j-1]:
            if 0 <= a < n and 0 <= b < m and (a,b) not in visit and (a,b) in minerals:
                visit.add((a,b))
                check.add((a,b))
                q.append((a,b))
    return [land, visit, check]

# 현재 떨어질 미네랄이 있는지 판단, 있다면 떨어질 미네랄 좌표 리턴
def cluster():
    visit = set()
    sky_cluster = set()

    for mineral in minerals:
        if mineral not in visit:
            [land, visit, check] = find(mineral, visit)
            if land == False:
                sky_cluster.update(check)
    
    return sky_cluster if sky_cluster else False

# 떨어질 미네랄의 좌표를 이용해서 떨어질 길이를 구한다.
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

# 막대기를 던져 미네랄의 위치 변경 
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

# 현재 남아 있는 미네랄의 좌표를 이용하여 새로운 보드 생성
result = [['.']*m for _ in range(n)]
for x,y in minerals:
    result[x][y] = 'x'
for i in result:
    print(''.join(i))

# 방문 체크를 큐에서 꺼낼때 하지말고 큐에 넣을때 하니 통과했다. 히히