import sys
sys.setrecursionlimit(10**6) # 백준에서 재귀가 오류가 나와서 추가
input = sys.stdin.readline

test_case = int(input())

# 지렁이 함수를 만들어서 dps를 통해 주변 배추를 0으로 만듬
def worm(x,y): 
    farm[x][y] = 0
    for a,b in [x+1, y],[x-1, y],[x, y+1],[x, y-1]:
        if 0 <= a < h and 0 <= b < w and farm[a][b] == 1:
            worm(a,b)

# 농장을 0,0 부터 h,w까지 확인하면 배추가 있으면 지렁이 함수호출. 함수가 몇번 호출됬는지 리턴
def result(w,h):
    count = 0
    for i in range(h):
        for j in range(w):
            if farm[i][j] == 1:
                worm(i,j)
                count += 1
    return count

for _ in range(test_case):
    w,h,c = map(int,input().split())
    farm = [[0] * w for _ in range(h)]

    # 뭔가 이문제 테스트 케이스가 좌표가 이상하다.. y,x순서로 값을 받음
    for _ in range(c):
        y,x = map(int,input().split())
        farm[x][y] = 1

    print(result(w,h))
    
