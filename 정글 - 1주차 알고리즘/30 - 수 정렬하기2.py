import sys
input = sys.stdin.readline


n = int(input())
nums = [int(input()) for _ in range(n)]

# # 그냥 sort()함수 쓰면됨...
# nums.sort()
# print(*nums, sep='\n')

# merge sort 통과함 시간은 많이 늘었지만...
def merge(arr):
    n = len(arr)
    if n < 2:
        return arr
    mid = n // 2
    left_arr = merge(arr[:mid])
    right_arr = merge(arr[mid:])
    merge_arr = []
    x = 0
    y = 0
    while x < len(left_arr) and y < len(right_arr):
        if left_arr[x] > right_arr[y]:
            merge_arr.append(right_arr[y])
            y += 1
        else:
            merge_arr.append(left_arr[x])
            x += 1
    merge_arr += left_arr[x:]
    merge_arr += right_arr[y:]
    return merge_arr
print(*merge(nums),sep='\n')



# 퀵 정렬  메모리 초과 
# sys.setrecursionlimit(10**6) -> Python이 정한 최대 재귀 갚이를 변경할 수 있습니다.
# def quick(arr):
#     if len(arr) < 2:
#         return arr
#     mid = len(arr) // 2
#     front_arr = []
#     mid_arr = []
#     end_arr = []
#     for i in arr:
#         if arr[mid] < i:
#             end_arr.append(i)
#         elif arr[mid] > i:
#             front_arr.append(i)
#         else:
#             mid_arr.append(i)
#     return quick(front_arr) + mid_arr + quick(end_arr) # quick(mid_arr)을 안하는 이유는 mid_arr에 같은 값이 들어가면 무한 루프에 빠진다.
# result = quick(nums)
# print(*result, sep='\n')


# 버블 정렬(실패함 시간 초과)
# for i in range(n):
#     for j in range(n-i-1):
#         if nums[j] > nums[j+1]:
#             nums[j],nums[j+1] = nums[j+1],nums[j]

# for i in nums:
#     print(i)
