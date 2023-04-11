def solution(stones, k):
    start = 0
    end = max(stones)
    n = len(stones)
    
    while start <= end:
        mid = (start + end) // 2
        
        check = 0
        for i in range(n):
            if stones[i] <= mid:
                check += 1
            else:
                check = 0
            if check == k:
                end = mid -1
                break
        else:
            start = mid + 1
    
    return start


# 성능은 더 좋았는데 한개의 테스트를 통과하지 못함...
# from collections import deque

# def solution(stones, k):
#     q = deque(stones[:k])
#     check = max(q)
#     result = check

#     for i in range(k,len(stones)):
#         q.append(stones[i])
#         if check == q.popleft():
#             check = max(q)
#             result = min(result, check)
            
#     return result

# 살짝 꼼수이기는 하지만 이분탐색 말고 다른 방법으로 효율성을 확 올렸다.
# def solution(stones, k):
#     result = float('inf')
#     check = []
    
    # 오름차순으로 계속 올라가거나 내임차순으로 계속 내려가는 것에서 시간초과가 나는 로직이라 따로 처리해주었다.
#     for i in range(1,len(stones)):
#         if stones[i-1] < stones[i]:
#             stones = stones[i-1:]
#             break
#     else:
#         return stones[-k]
    
#     for i in range(len(stones)):
#         if stones[i] < result:
#             check.append(stones[i])
#         else:
#             check = []
#         if len(check) == k:
#             result = max(check)
#             check = check[check.index(result)+1:]            
#     return result