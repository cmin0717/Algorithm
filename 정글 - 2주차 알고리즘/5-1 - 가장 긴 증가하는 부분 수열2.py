import sys
# from bisect import *
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

result = [nums[0]]

def bisect_lefr(arr,find):  # 이분 탐색을 이용한 위치 찾기
    left,right = 0, len(arr)-1  # 주어진 arr의 0 , 끝 인덱스를 지정
    while left <= right: 
        mid = (left + right) // 2
        if arr[mid] >= find: # 같은 값도 처리해줘야 하기에 >= 사용
            right = mid - 1
        else:
            left = mid + 1
    return left # 왼쪽 인덱스가 필요하기에 left 반환

for i in nums[1:]:
    if result[-1] < i:
        result.append(i)
    else:
        idx = bisect_lefr(result,i)
        result[idx] = i

print(len(result))


# 라이브러리 bisect 이용
# bisect_left(x,y) -> x 리스트에서 i 값보다 작은수 앞 인덱스를 반환한다.
# bisect_right(x,y) -> x 리스트에서 i 값보다 바로 앞 큰수 뒤 인덱스를 반환

# for i in nums[1:]:
#     if result[-1] < i:
#         result.append(i)
#     else:
#         idx = bisect_left(result,i)
#         result[idx] = i

# print(len(result))