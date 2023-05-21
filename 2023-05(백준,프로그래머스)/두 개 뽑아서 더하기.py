from itertools import combinations

def solution(numbers):
    
    nums = set([sum(i) for i in combinations(numbers,2)])
    
    return sorted(list(nums))