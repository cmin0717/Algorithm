import sys
input = sys.stdin.readline

sanggn = int(input())
sanggn_nums = list(map(int,input().split()))
sanggn_nums.sort() # 이분 탐색을 위해 정렬

m = int(input())
m_nums = list(map(int,input().split()))

def check(arr, start, end, find):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == find: # 찾는 값이 있다면 바로 리턴
            return 1
        elif arr[mid] < find:
            start = mid +1
        else:
            end = mid - 1
    return 0 # 다 찾아봣는ㄴ데 없었다면 0 리턴

start = 0
end = sanggn-1
result = []

for i in range(m):
    result.append(check(sanggn_nums,start,end,m_nums[i]))

print(*result)

# set자료형을 사용하면 이문제는 더 빠르게 풀수있다.