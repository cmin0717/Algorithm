import sys
input = sys.stdin.readline

n,m = map(int, input().split())

trees = list(map(int,input().split()))
max_high = max(trees) # 최대 나무 높이를 설정 이분 탐색 end부분
min_high = 0

def check(arr,start,end,find):
    while start <= end: # 시작이 end를 넘어가게 되면 그 전 부분을 출력할것이다.
        mid = (start + end) // 2
        cut_tree = 0

        for i in arr: # 잘린 나무를 cut_tree에 담아준다
            if i > mid:
                cut_tree += i -mid

        if cut_tree >= find: # cut_tree가 같다면 넘겨줘도 어차피 다시 줄어든 값을 리턴하기떄문에 걱정하지 않아도 된다.
            start = mid + 1
        else:
            end = mid - 1
    return end

print(check(trees,0,max_high,m))



# 파이썬은 시간초과 pypy3는 통과
# while min_high <= max_high:

#     mid = (min_high + max_high) // 2
#     cut_tree = 0

#     for i in trees:
#         if i > mid:
#             cut_tree += i - mid

#     if cut_tree > m:
#         min_high = mid + 1
#     elif cut_tree < m:
#         max_high = mid - 1
#     else:
#         max_high = mid
#         break

# print(max_high)


# 통과는 했는데 뭔가 만족스럽지 못함
# max_tree = []
# for i in trees:
#     heapq.heappush(max_tree, -i)

# max_high = abs(max_tree[0])

# def check(arr,start,end,find):
#     while start <= end:
#         mid = (start + end) // 2
#         cut_tree = 0
#         cut_cnt = 0
#         for i in arr:
#             if i > mid:
#                 cut_cnt += 1
#                 cut_tree += i - mid
#         if cut_tree > find+cut_cnt-1:
#             start = mid
#         elif cut_tree < find:
#             end = mid
#         else:
#             break
#     return mid
 
# print(check(trees, 0, max_high, m))



# 시간 초과 (재귀를 써서 그런듯)
# def check(arr,start,end,find):
#     global result
#     mid = (start + end) // 2
#     cut_tree = 0
#     for i in arr:
#         if i > mid:
#             cut_tree += i - mid
#     if cut_tree > find:
#         check(arr, mid+1, end, find)
#         return
#     elif cut_tree < find:
#         check(arr, start, mid-1, find)
#         return
#     else:
#         result += mid
#         return

# check(trees,0,max_high,m)
# print(result)