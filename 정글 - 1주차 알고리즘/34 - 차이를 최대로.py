from itertools import *

n = int(input())
nums = list(map(int,input().split()))

def check(a):
    num = 0
    for i in range(len(a)-1):
        num += abs(a[i]-a[i+1])
    return num

li = list(permutations(nums,n)) # permutation으로 모든 경우의 순열을 뽑는다.

max_nums = []

for i in li:
    max_nums.append(check(i)) # check()함수를 이용하여 해당 순열의 값을 max_nums에 저장한다.

print(max(max_nums))
