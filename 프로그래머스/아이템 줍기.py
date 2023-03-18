from collections import deque

def check(arr, i, j):
    for x,y,x1,y1 in arr:
        if x*2 < j < x1*2 and y*2 < i < y1*2:
            return False
    return True

def solution(r, cx, cy, ix, iy):
    box = [[0] *101 for _ in range(101)]
    for x,y,x1,y1 in r:
        for i in range(y*2,y1*2+1):
            box[i][x*2] = 1
            box[i][x1*2] = 1
        for i in range(x*2,x1*2+1):
            box[y*2][i] = 1
            box[y1*2][i] = 1
    box[cy*2][cx*2] = 0
    box[iy*2][ix*2] = -1

    result = []
    q = deque([[cy*2,cx*2,0]])
    while q:
        x,y,cnt = q.popleft()
        for a,b in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
            if 0 <= a < 101 and 0 <= b < 101 and box[a][b] != 0:
                if a == iy*2 and b == ix*2:
                    result.append(cnt+1)
                    continue
                if check(r,a,b):
                    box[a][b] = 0
                    q.append([a,b,cnt+1])
                    
    return min(result) // 2