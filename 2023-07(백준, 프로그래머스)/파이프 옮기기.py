import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0,0,0] for _ in range(n)] for i in range(n)]
dp[0][1][0] = 1

def validate(x,y):
    if 0 <= x < n and 0 <= y < n and board[x][y] == 0:
        return True
    return False

def find(x,y):
    col, row = 0, 0
    if validate(x,y-1):
        col += dp[x][y-1][0] + dp[x][y-1][2]
    if validate(x-1,y):
        row += dp[x-1][y][1] + dp[x-1][y][2]
    return col, row

def dia(x,y):
    if validate(x,y) and validate(x-1,y) and validate(x,y-1) and validate(x-1,y-1):
        cost = sum(dp[x-1][y-1])
        return cost
    else:
        return 0

for i in range(n):
    for j in range(n):
        if i == 0 and (j == 0 or j == 1): continue
        if validate(i,j):
            c, r = find(i,j)
            dp[i][j][0] = max(c, dp[i][j][0]) 
            dp[i][j][1] = max(r, dp[i][j][1])
            dp[i][j][2] = max(dia(i,j), dp[i][j][2])
print(sum(dp[n-1][n-1]))
















# ex = {1: [[0,1,1], [1,1,3]], 2: [[1,0,2], [1,1,3]], 3: [[0,1,1], [1,1,3], [1,0,2]]}

# def range_check(x,y):
#     if 0 <= x < n and 0 <= y < n and board[x][y] == 0:
#         return True
#     return False

# def move_check(x,y):
#     if range_check(x+1,y+1) and range_check(x+1,y) and range_check(x,y+1):
#         return True
#     return False

# def find(b, d):
#     arr = []

#     for dx,dy,dist in ex[d]:
#         i= b[0]+dx
#         j = b[1]+dy
#         if dist != 3 and range_check(i,j):
#             arr.append([(i,j), dist])
#         elif dist == 3 and move_check(b[0], b[1]):
#             arr.append([(i,j), dist])

#     return arr

# q = deque([[(0,1), 1]])
# result, end = 0, (n-1,n-1)

# while q:
#     now, dist = q.popleft()
#     if now == end:
#         result += 1
#         continue

#     for info in find(now, dist):
#         q.append(info)
# print(result)

