from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

basis = [i for i in range(1,n+1)] # 기본 부품을 확인하고 저장하기 위해 만듬
link = [[] for _ in range(n+1)] # 연결 리스트
degree = [0] * (n+1) # 진입 차수

for _ in range(m):
    part = list(map(int,input().split()))
    link[part[1]].append(part)
    degree[part[0]] += 1
    if part[0] in set(basis): # 여기서 part[0]은 중간부품에 해당하므로 basis에서 빼준다.
        basis.remove(part[0])

dp = [[0]* (n+1) for _ in range(n+1)] # 부품을 더하기위해 dp를 사용했다.
dq = deque()

for i in range(len(basis)): # 기본 부품들은 dp에 각자 부분만 +1 해주고 dq에 기본 부품를 넣어준다. 기본 부품은 진입 차수가 0이기에
    a = basis[i]
    dp[a][a] += 1
    dq.append(a)

while dq: # 위상 정렬을 한다.
    idx = dq.popleft()
    for x,y,z in link[idx]:

        degree[x] -= 1
        if degree[x] == 0: # 진입 차수가 0이 되면 dq에 넣어준다.
            dq.append(x)

        for i in range(1,n+1): # dp를 이용하여 부품개수를 더해준다.
            if dp[y][i] != 0:
                dp[x][i] += dp[y][i] * z

for i in range(len(dp[-1])): # i가 basis에 있다면 기본 부품이기에 출력
    if i in basis:
        print(f'{i} {dp[-1][i]}')

# 문제를 완전히 이해하기에 시간이 쫌 걸렸다.....
# 기본 부붐은 주어진 중간 부품에 없는 애들이 다 기본 부품이다.