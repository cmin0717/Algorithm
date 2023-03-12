import sys
input = sys.stdin.readline

n,m = map(int,input().split())

floor = [input().rstrip() for _ in range(n)]
check = [[0] * m for _ in range(n)] # 방문 체크

deck_cnt = 0 # 장식수

def deck(x,y,p): # 함수에 [x좌표, y좌표, 패턴]을 넣어준다.
    if p == '-':
        check[x][y] = 1 #방문 체크
        for a,b in [x,y-1],[x,y+1]:
            if 0 <= b < m and check[a][b] == 0 and floor[a][b] == p: # 조건에 만족하면 진행
                deck(a,b,p)
    else:
        check[x][y] = 1
        for a,b in [x-1,y],[x+1,y]:
            if 0 <= a < n and check[a][b] == 0 and floor[a][b] == p:
                deck(a,b,p)

for i in range(n):
    for j in range(m):
        if floor[i][j] == '-' and check[i][j] == 0: # 패턴이 있고 방문을 안했다면 진행
            deck(i,j,'-')
            deck_cnt += 1 # 함수를 실행 했다면 장식이 있는거니깐 +1
        if floor[i][j] =='|' and check[i][j] == 0:
            deck(i,j,'|')
            deck_cnt += 1
print(deck_cnt)