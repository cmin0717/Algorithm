def solution(b, y):
    nums = []
    for i in range(1,round(y**0.5)+1):
        if y % i == 0:
            nums.append([y//i, i])
            nums.append([i, y//i])
    for i in range(len(nums)):
        if b-4 == sum(nums[i]) * 2:
            result = sorted([nums[i][0]+2, nums[i][1]+2], reverse=True)
            return result
        
print(solution(10, 2))