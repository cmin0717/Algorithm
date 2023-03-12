import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]
cnt_1, cnt_0 = 0, 0 # 잘린 1과 0의 개수를 저장

def cut(x,y,m):
    global cnt_1,cnt_0
    standard = paper[x][y] # 시작을 뭘로 하냐를 저장

    for i in range(x,x+m):
        for j in range(y,y+m):
            if paper[i][j] != standard: # paper를 확인하면서 시작과 다르면 4등분 절단
                new_m = m//2 # 4등분 절단하니깐 m값도 달라져야한다.
                cut(x, y, new_m)
                cut(x+new_m, y, new_m)
                cut(x, y + new_m, new_m)
                cut(x+new_m, y+new_m, new_m)
                return # 절단 후 retrun으로 함수 종료

    if standard == 1: # 절단 되지 않고 끝까지 for문을 통과했다면 시작점에 해당하는 cnt에 +1 해준다.
        cnt_1 += 1
    else:
        cnt_0 += 1

cut(0,0,n)
print(cnt_0, cnt_1, sep='\n')