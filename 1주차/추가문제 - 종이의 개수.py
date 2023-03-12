import sys
imput = sys.stdin.readline

n = int(input())

paper = [list(map(int,input().split())) for _ in range(n)]

# 각 -1,0,1의 개수를 저장
cnt_0 = 0 
cnt_1 = 0
cnt_2 = 0

def check(x,y,n):
    global cnt_0,cnt_1,cnt_2

    standard = paper[x][y] # 시작점을 정해준다.

    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j] != standard: # 시작점과 다르면 분할
                new_n = n // 3
                check(x, y, new_n)
                check(x+new_n, y, new_n)
                check(x+(new_n*2), y, new_n)
                check(x, y+new_n, new_n)
                check(x, y+(new_n*2), new_n)
                check(x+new_n, y+new_n, new_n)
                check(x+(new_n*2), y+new_n, new_n)
                check(x+new_n, y+(new_n*2), new_n)
                check(x+(new_n*2), y+(new_n*2), new_n)
                return # 분할했다면 리턴으로 함수 종료
    else:
        if standard == 1: # 시작점에 해당하는 곳에 +1
            cnt_1 += 1
        elif standard == 0:
            cnt_0 += 1
        else: cnt_2 += 1
check(0,0,n)
print(cnt_2,cnt_0,cnt_1,sep='\n')