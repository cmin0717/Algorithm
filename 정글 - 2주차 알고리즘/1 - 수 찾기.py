import sys
input = sys.stdin.readline

n = int(input())
# n_nums = set(map(int, input().split())) # n_nums에서 찾아야 하니깐 set자료형으로 저장
n_nums = list(map(int, input().split()))
m = int(input())
m_nums = list(map(int, input().split()))

# set자료형을 이용한 풀이
# for i in m_nums:
#     if i in n_nums: # set자료형에서 in 은 o(1)시간 복잡도를 가진다.
#         print(1)
#     else:
#         print(0)

def check(arr,start,end,find): # 중간 인덱스를 기준으로 크면 우 작으면 좌로 점점 좁혀가면서 찾아간다.
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < find:
            start = mid+1
        elif arr[mid] > find:
            end = mid-1
        else:
            return mid
    return None

n_nums.sort() # 정렬된 배열에서 해야한다.

for i in m_nums:
    if check(n_nums,0,n-1,i) != None:
        print(1)
    else:
        print(0)