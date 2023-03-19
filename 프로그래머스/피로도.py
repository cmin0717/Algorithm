result = 0

def check(arr,k,visit):
    global result
    result = max(result, len(visit))
    for i in range(len(arr)):
        if i not in visit and k-arr[i][0] >= 0:
            check(arr,k-arr[i][1],visit + [i])

def solution(k, dungeons):
    global result
    check(dungeons,k,[])
    return result

# 함수 안에 새로운 함수 선언해서 풀이(시간은 이게 조금더 빠르게 나옴)
# def solution(k, dungeons):
#     result = []
#     def check(arr,k,visit):
#         result.append(len(visit))
#         for i in range(len(arr)):
#             if i not in visit and k-arr[i][0] >= 0:
#                 check(arr,k-arr[i][1],visit + [i])
#     check(dungeons,k,[])
#     return max(result

print(solution(80,[[80,20],[50,40],[30,10]]))