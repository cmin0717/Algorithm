from itertools import *

n,m = map(int, input().split())

nums = list(map(int, input().split()))

cnt = 0

for i in range(1,n+1): # 조합이 1 ~ n개일때 다 확인해주어야 하기 때문에
    for j in combinations(nums,i): # 조합의 원소 개수가 i개일때 나올수있는 모든 수 확인
        if sum(j) == m:
            cnt += 1
print(cnt)