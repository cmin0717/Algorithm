from copy import deepcopy
from itertools import *
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
lab_map = []
map_0 = []
virus = []
for i in range(n):
    maps = list(map(int,input().split()))
    lab_map.append(maps)
    for j in range(m):
        if maps[j] == 0:
            map_0.append([i,j]) # 0이 위치한 좌표를 o_map에 저장해둔다.
        elif maps[j] == 2:
            virus.append([i,j]) # 바이러스가 위치한 좌표를 virus에 저장

def save_cnt(arr): # 벽과 바이러스가 다 퍼지고난후 안전지역의 수를 파악하는 함수를 만들어준다.
    save_arr = arr
    cnt = 0
    for i in range(n):
        for j in range(m):
            if save_arr[i][j] == 0:
                cnt += 1
    return cnt

def dsf(x,y,cp_map):  # 벽을 만든후 바이러스가 퍼질수있도록 함수를 만들어준다.
    for i,j in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
        if 0 <= i < n and 0 <= j < m and cp_map[i][j] == 0:
            cp_map[i][j] = 2
            dsf(i,j,cp_map)
max_save = 0
for li in combinations(map_0,3): # 아까 저장한 0의 좌표값으로만 combination을 이용하여 3개를 뽑아 벽을 세워준다.
    cp_map = deepcopy(lab_map)
    cp_virus = deepcopy(virus)
    for i,j in li:
        cp_map[i][j] = 1
    while cp_virus:
        x,y = cp_virus.pop()
        dsf(x,y,cp_map)
    max_save = max(save_cnt(cp_map), max_save)
print(max_save)
    
