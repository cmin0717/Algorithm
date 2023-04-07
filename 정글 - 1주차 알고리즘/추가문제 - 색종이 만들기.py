import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)] 
arr_1 = 0 # 0 색종이 개수
arr_2 = 0 # 1 색종이 개수

def slice_paper(x,y,n):
    global arr_1,arr_2

    standard = paper[x][y] # 시작점이 0인지 1인지 확인

    for i in range(x,x+n): # range의 끝을 잘 정해주어야한다. 주어진 사분면만 확인하기 위해 n 대신 x+n사용
        for j in range(y,y+n):
            if paper[i][j] != standard: # 시작점과 다르다면 쪼개주어야 한다.
                new_n = n//2
                slice_paper(x, y, new_n) # 1사분면
                slice_paper(x+new_n, y, new_n) # 2사분면
                slice_paper(x, y+new_n, new_n) # 3사분면
                slice_paper(x+new_n, y+new_n, new_n) # 4사분면
                return # 다 쪼개서 넣어줬다면 함수 종료
    else:
        if standard == 0: # 시작점에 따라 0,1에 1을 더해준다.
            arr_1 += 1
        else:
            arr_2 += 1

slice_paper(0,0,n) # 0,0부터 시작

print(arr_1,arr_2,sep='\n')