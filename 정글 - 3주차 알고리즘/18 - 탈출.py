import sys
input = sys.stdin.readline # 이문제는 큐를 사용하지 않고 해결가능하다.

row,col = map(int,input().split())

road_map = [input().rstrip() for _ in range(row)]
maps = [[]*col for _ in range(row)]
dq_w = [] # 물이 시작하는 좌표저장
dq_d = [] # 고슴도치 시작점 저장
d = [] 
time = 0 # 분을 체크하는 변수
for i in range(row): # 주어진 road_map를 사용하기 편하게 바꾸어 주면서 필요한 정보들 저장
    for j in range(col):
        if road_map[i][j] == '*':
            dq_w.append([i,j])
            maps[i].append('*')
        elif road_map[i][j] == 'S':
            dq_d.append([i,j])
            maps[i].append(time)
        elif road_map[i][j] == 'D':
            maps[i].append('D')
        elif road_map[i][j] == 'X':
            maps[i].append('X')
        else:
            maps[i].append('.')

def dochi(arr,time): # 도치가 움직이는 함수 (리스트를 통쨰로 받아오고 return값에 새로운 도치 좌표를 넣어서 전달)
    move_dochi = []
    for x,y in arr:
        for a,b in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
            if 0 <= a < row and 0 <= b < col:
                if maps[a][b] == '.': # 아무것도 없는곳이면 움직인 시간을 넣어준다.
                    maps[a][b] = time+1
                    move_dochi.append([a,b])
                elif maps[a][b] == 'D': # 동굴에 도착하면 도착시간을 d리스트에 넣어준다.
                    d.append(time+1)
    return move_dochi

def water(arr): # 물이 퍼지는 함수 (위와 같이 리스트를 통째로 받아오고 새로운 물 좌표를 전달)
    move_water = []
    for x,y in arr:
        for a,b in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
            if 0 <= a < row and 0 <= b < col:
                if maps[a][b] != '*' and maps[a][b] != 'D' and maps[a][b] != 'X':
                    maps[a][b] = '*'
                    move_water.append([a,b])
    return move_water

while dq_d:
    dq_w = water(dq_w) # 물이 잠길 곳에 도치는 갈수없기에 물 먼저 하고 그다음 도치가 움직인다.
    dq_d = dochi(dq_d,time)
    time += 1 # 다 했으면 시간을 +1

if d:
    print(min(d)) 
else:
    print('KAKTUS') # 만일 리스트가 비어있다면 도치가 동굴에 못가고 죽었으니깐 kaktus출력

