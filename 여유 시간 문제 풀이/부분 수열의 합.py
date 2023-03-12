from itertools import *
import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int,input().split()))
result = {*nums} # set자료형에 초기값으로 nums를 넣어준다.

for i in range(2,n+1):  # 원소가 2개인 부분수열부터 더해서 set자료형에 넣어준다.
    for num in combinations(nums, i):
        result.add(sum(num))

for i in range(1,sum(nums)+2): # 1부터 확인하여 없으면 i출력
    if i not in result:
        print(i)
        break


# 시간이 되게 짧은 풀이인데 왜 이게 되는지는 아직 잘모르겠다.
# nums = list(map(int,input().split()))
# nums.sort()

# sum = 1
# for i in nums:
#     if sum < i:
#         print(sum)
#         break
#     sum += i
# else:
#     print(sum)

