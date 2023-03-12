import sys
sys.setrecursionlimit(10**6) # 이번 문제에서는 재귀 깊이를 설정 안해주면 RecursionError에러가 나온다.
input = sys.stdin.readline

n,m = map(int,input().split())

li = [[] for _ in range(n+1)] # 각 번호에 해당하는 리스트 생성
result = [0] * (n+1) # 방문 했었는지 확인하는 리스트

for _ in range(m):
    x,y = map(int,input().split())
    li[x].append(y) # 연결된 양 방향으로 값을 넣어준다.
    li[y].append(x)

def check(x):
    result[x] = 1
    for i in li[x]:
        if result[i] == 0: # 방문을 한번도 안했다면 check함수 실행
            check(i)

cnt = 0
for i in range(1,n+1):
    if result[i] == 0: # 방문을 안했다면 check함수 실행
        check(i)
        cnt += 1 # check함수가 실행되면 i랑 연결된 모든 곳은 다 연결되므로 cnt += 1 해준다

print(cnt)