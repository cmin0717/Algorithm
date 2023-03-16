import sys
input = sys.stdin.readline

nums = list(map(int,input().split()))

def solution(nums):
    n = len(nums) // 2 
    m = len(set(nums))

    return (n if m > n else m)

print(solution(nums))