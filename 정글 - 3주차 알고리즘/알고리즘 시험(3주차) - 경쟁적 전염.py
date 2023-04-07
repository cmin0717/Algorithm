import sys
input = sys.stdin.readline

n,k = map(int,input().split())

test = [list(map(int,input().split())) for _ in range(n)] # 시험관 저장

s,x,y = map(int,input().split()) # 시간,좌표 저장

virus = [[] for _ in range(k+1)] # 각 바이러스 좌표 저장

for i in range(n):
    for j in range(n):
        if test[i][j] != 0: # 시험관을 돌면서 초반 바이러스 좌표를 가져온다.
            virus[test[i][j]].append([i,j])

def infection(x): # 전염시키는 함수
    new_virus = [] # 전염 이후의 바이러스 좌표
    for a,b in virus[x]: # x 바이러스 좌표를 꺼내온다
        for i,j in [a+1,b],[a-1,b],[a,b+1],[a,b-1]:
            if 0 <= i < n and 0 <= j < n and test[i][j] == 0: #조건에 만족하면 진행
                test[i][j] = x
                new_virus.append([i,j]) # 새로운 바이러스 좌표를 저장
    return new_virus 

for _ in range(s):
    for i in range(1,k+1):
        virus[i] = infection(i) # 새로운 바이러스 좌표로 갱신시킨다.

print(test[x-1][y-1])