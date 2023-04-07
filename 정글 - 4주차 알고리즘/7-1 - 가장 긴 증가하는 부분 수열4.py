n =  int(input())

nums = list(map(int,input().split()))

dp = [1] * n

for i in range(n): # 가장 긴 증가하는 부분 수열의 길이를 구한다.
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

max_dp = max(dp)
result = []
find = max_dp # 앞쪽 부터 찾는게 아니라 뒤에서 부터 찾는다.

while True:
    for i in range(n-1,-1,-1):
        if dp[i] == find: # 찾는 순번의 숫자가 나오면
            result.append(nums[i])
            n = i # for문 시작점을 바꾸어주고
            find -= 1 # 찾는 순번을 -1 해준다.
            break
    if len(result) == max_dp: # 만약 가장 긴 증가수열의 길이만큼 추가 했다면 종료
        break

print(max_dp)
print(*result[::-1]) # 반대로 들어가있으니깐 출력은 바꾸어서 해준다.


