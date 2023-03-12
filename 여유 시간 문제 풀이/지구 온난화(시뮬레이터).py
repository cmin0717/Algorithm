import sys
input = sys.stdin.readline

r,c = map(int,input().split())

sea = []
land = []
for i in range(r):
    m = ['.'] + list(map(str,input().rstrip())) + ['.'] # 영역 패딩
    sea.append(m)
    for j in range(c+2):
        if sea[i][j] == 'X':
            land.append([i+1,j])
sea = [['.'] * (c+2)] + sea + [['.'] * (c+2)] # 영역 패딩

new_land = []
result = []

while land:
    x,y = land.pop()
    check = 0
    for i,j in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
        if sea[i][j] == '.':
            check += 1
    if check >= 3:
        new_land.append([x,y]) # 잠긴 땅
    else:
        result.append([x,y]) # 살아남은 땅
else:
    for x,y in new_land:
        sea[x][y] = '.' # 잠긴 땅이니깐 표시

land_0 = sorted(result, key=lambda x: x[0]) # 해당 영역만 표시하기위해 가로 세로 구함
land_1 = sorted(result, key=lambda x: x[1])
x = land_0[0][0]
y = land_0[-1][0]
a = land_1[0][1]
b = land_1[-1][1]
for i in range(x,y+1):
    print(''.join(sea[i][a:b+1]))

