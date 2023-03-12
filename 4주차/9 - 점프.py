from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

obstacle = set([int(input()) for _ in range(m)])

dp = [[float('inf')] * (int((2 * n)**0.5) +2) for _ in range(n+1)] # 각 돌 위치에서 최대 점프 거리만큼 dp를 2차배열로 만들어준다.
dp[1][0] = 0 # 처음 시작점은 0으로 세팅

for i in range(2,n+1):
    if i in obstacle: # 이상한 돌 만나면 패쓰
        continue
    for j in range(1, int((2 * i) ** 0.5) + 1): # 1 부터 i위치 에서 제일 멀리 점프할수있는 높이 까지 dp로 값을 넣어준다.
        dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1 

if min(dp[n]) == float('inf'):
    print(-1)
else:
    print(min(dp[n]))

# V * (V + 1) / 2 = N
# V ** 2 + V = 2N 
# V = (2N - V) ** 0.5 < 2N ** 0.5
# 결국 길이가 n인 길이에서 초항이 1이고 공차가 1인 등차수열의 합은 점화식으로 풀면
# 어쩌구 저쩌구 되서 (2 * n) **0.5가 계속 늘었났을떄 최대값이다. 결국 n길이 에서 제일 멀리 뛰는게 저 값이다.
# ----------------------------------------------------------------------------------------------
# bfs 풀이법

dq = deque()
dq.append([1,0,0])
check = [[] for _ in range(n+1)]

while dq:
    idx,len,cnt = dq.popleft()
    for i in [-1,0,1]:
        new = len + i
        if new < 1:continue
        if idx + new == n:
            print(cnt+1)
            exit()
        if idx+new < n and idx+new not in obstacle and new not in check[idx+new]:
            check[idx+new].append(new)
            dq.append([idx+new, new, cnt+1])
else:
    print(-1)