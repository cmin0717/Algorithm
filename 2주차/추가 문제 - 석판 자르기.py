import sys
input = sys.stdin.readline

n = int(input())

stone = []
jam_cnt = 0
for _ in range(n):
    slate = list(map(int,input().split()))
    stone.append(slate)
    if slate.count(2):
        jam_cnt += slate.count(2)

success = 0

def row_cut(x,y,r,c,i):
    if i == x or i == r-1:
        return False
    if 2 in stone[i][y:c]:
        return False
    return True

def col_cut(x,y,r,c,j):
    if j == y or j == c-1:
        return False
    if 2 in [stone[i][j] for i in range(x,r)]:
        return False
    return True

def cut_stone(x,y,r,c,check):
    global cnt
    jam = 0
    impurities = 0
    for i in range(x, r):
        for j in range(y, c):
            if stone[i][j] == 2:
                jam += 1
            if stone[i][j] == 1:
                impurities += 1
                if check == 1:
                    if col_cut(x,y,r,c,j):
                        cut_stone(x, y, r, j, 0)
                        cut_stone(x, j+1, r, c, 0)
                else:
                    if row_cut(x,y,r,c,i):
                        cut_stone(x, y, i, c, 1)
                        cut_stone(i+1, y, r, c, 1)
    if jam == 1 and impurities == 0:
        cnt += 1

check_im = 0
for i in range(n):
    for j in range(n):
        if stone[i][j] == 1:
            check_im += 1
            if row_cut(0,0,n,n,i):
                cnt = 0
                cut_stone(0, 0, i, n, 1)
                cut_stone(i+1, 0, n, n, 1)
                if cnt == jam_cnt:
                    success += 1
            if col_cut(0,0,n,n,j):
                cnt = 0
                cut_stone(0, 0, n, j, 0)
                cut_stone(0, j+1, n, n, 0)
                if cnt == jam_cnt:
                    success += 1
if check_im == 0 and jam_cnt == 1:
    success += 1

if success != 0:
    print(success)
else:
    print(-1)

# 맞는거 같은데 반례가 없으니깐 확인할수가 없다...슈발,,,,나중에 다시 확인 해보자