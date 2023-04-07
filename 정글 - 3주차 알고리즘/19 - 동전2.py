import sys
input = sys.stdin.readline

n,k = map(int,input().split())

coin = [int(input()) for _ in range(n)]

dp = [1 if i in set(coin) else float('inf') for i in range(k+1)] # 최소값을 구하는 거니깐 dp초기값을 무한대로 주고 가지고 있는 동전은 1로 둔다.

for i in range(1,k+1): # 1부터 목표 돈까지 진행
    if dp[i] != 1: # 값이 1이면 최저값이기에 패쓰!
        for j in coin:
            if i - j < 0:continue # 현재 돈보다 가지고 있는 동전이 크다면 음수가 나오니깐 패쓰!
            dp[i] = min(dp[i], dp[j] + dp[i-j]) # 현재 dp값과 [현재값 - 가진 동전의 원 + 1]과 비교해서 더 작은값 저장

if dp[-1] == float('inf'): # 목표 돈을 만들수 없다면 -1 출력
    print(-1)
else:
    print(dp[-1])
