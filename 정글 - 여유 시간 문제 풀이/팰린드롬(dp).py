import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
dp = [[False]*n for _ in range(n)]

for i in range(n): # 길이가 1이나 2인 수를 먼저 체크한다.
    dp[i][i] = True
    if i+1 < n:
        if nums[i] == nums[i+1]:
            dp[i][i+1] = True

for distance in range(n-2): # 서로의 거리을 나타내는 변수
    for i in range(n-2-distance):
        j = distance + i + 2 # j를 직접 정해주어야한다.
        if nums[i] == nums[j] and dp[i+1][j-1]: # 양쪽이 같고 양쪽 바로 앞이 참이면 팰린드롬이다.
            dp[i][j] = True

for _ in range(int(input())):
    x,y = map(int,input().split())
    print(+dp[x-1][y-1]) # bool값을 출력 할 때 +을 붙히면 정수로 출력가능하다.
        


