import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

result = [nums[0]] # 일단 0번째 인덱스를 넣어주고 시작

for i in nums[1:]:
    if result[-1] < i: # result[-1] 보다 i가 크다면 i 추가
        result.append(i)
    else:
        for j in range(len(result)):
            if i <= result[j]:
                result[j] = i # result[j] 보다 i가 작다면 result[j] 값에 i를 넣어준다.
                break

print(len(result)) # 부분 수열을 이루는 원소는 달라도 최대 길이는 같다.


# dp를 이용한 풀이법
# dp = [1] * n # 각 자리의 가장긴 부분수열의 길이를 저장할것이다. 처음에는 각각 1로 시작

# for i in range(n):
#     for j in range(i):
#         if nums[j] < nums[i]: # 만일 num[i]가 num[j]보다 크다면 j일때의 dp[j]에 +1한값이 dp[i]가 된다.
#             dp[i] = max(dp[i], dp[j]+1) # 무조건 dp[i] = dp[j] + 1이 아니라 dp[i]가 더 클수도 있기에 둘중 큰값을 넣어준다.

# print(max(dp)) 마지막으로 dp리스트에서 가장 큰값 출력

