import sys
from itertools import combinations
input = sys.stdin.readline

need = int(input())

n,m = map(int, input().split())

nums = [int(input()) for _ in range(n+m)]

start, end = 1, n+m
result = 0

while start < end:
    mid = (start + end) // 2

    count = 0
    for i in combinations(nums, mid):
        if sum(i) == need:
            count += 1
    
    if result > count:
        start = mid + 1
    else:
        result = count
        end = mid - 1

print(result)