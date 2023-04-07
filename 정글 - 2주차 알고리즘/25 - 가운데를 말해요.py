import sys
from heapq import *
input = sys.stdin.readline

n = int(input())

min_num = []
mid_num = []
max_num = []

for i in range(1,n+1):
    num = int(input())

    if i == 1: # 처음 받는 숫자는 그냥 바로 출력후 continue
        heappush(mid_num, num)
        print(mid_num[0])
        continue

    if num > mid_num[0]: # 입력 받은 숫자를 현재 중앙값에 대소 구분으로 넣어준다.
        heappush(max_num, num)
    else:
        heappush(min_num, -num)

    if len(max_num) - len(min_num) > 1: # 만약 현재 중앙값에 큰값이 작은값보다 2개이상이 되면
        heappush(min_num, -heappop(mid_num)) # 현재 중앙값을 min_num로 이동
        heappush(mid_num, heappop(max_num)) # max_num중 최소값을 중앙값으로 이동

    elif len(max_num) - len(min_num) < 0: # 만약 현재 중앙값에 비해 작은 값이 큰값보다 많아지면
        heappush(max_num, heappop(mid_num)) # 현재 중앙값 max_num로 이동
        m = heappop(min_num) # 최대값이 필요하기에 저장할때 -를 붙혀서 저장했다. 나올떄는 다시 -를 붙히고 원래값 출력
        heappush(mid_num, -m) # min_num의 최대값을 중앙값으로 이동 
 
    print(mid_num[0])




# 시간 초과
# for i in range(1,n+1):
#     num = int(input())
#     heapq.heappush(nums, num)
#     cp_nums = nums[:] # deepcopy보다 [:](list slicing)이 7배는 빠르다.
#     if i < 3:
#         print(nums[0])
#         continue
#     else:
#         if i % 2 == 0:
#             for _ in range(i//2-1):
#                 heapq.heappop(cp_nums)
#         else:
#             for _ in range(i//2):
#                 heapq.heappop(cp_nums)
#     print(cp_nums[0])
