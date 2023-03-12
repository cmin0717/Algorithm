import sys
input = sys.stdin.readline

# 추가 정보를 저장하는 리스트를 줄여 메모리 간소화
n = int(input())
cnt = [0] * 10001 

for i in range(n):
    m = int(input())
    cnt[m] += 1

for i in range(1,10001):
    for j in range(cnt[i]):
        print(i)

        


# 메모리 초과
# n = int(input())
# dp = [0] * 10001
# for i in range(n):
#     m = int(input())
#     dp[m] += 1

# cnt = 0
# for i in range(1,10001):
#     if dp[i]:
#         num = [i] * dp[i]
#         cnt += dp[i]
#         print(*num, sep='\n',end='\n')
#     if cnt == n:break
