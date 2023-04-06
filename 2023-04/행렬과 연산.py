from collections import deque
def solution(rc, op):
    # deque를 이용하여 좌,우측 열과 가운데 행을 저장
    left = deque([])
    right = deque([])
    mid = deque()
    for i in range(len(rc)):
        left.append(rc[i][0])
        right.append(rc[i][-1])
        mid.append(deque(rc[i][1:len(rc[0])-1]))

    for command in op:
        if command == 'Rotate':
            # 조건에 맞게 빼서 삽입
            mid[0].appendleft(left.popleft())
            right.appendleft(mid[0].pop())
            mid[-1].append(right.pop())
            left.append(mid[-1].popleft())
        else:
            # shift일시 뒤에서 빼서 앞으로 삽입
            left.appendleft(left.pop())
            right.appendleft(right.pop())
            mid.appendleft(mid.pop())
    
    result = []
    for i in range(len(rc)):
        print([left[i]] + list(mid[i]) + [right[i]])
        # result.append([[left[i]]+mid[i]+[right[i]]])
    print(result)

# 로직은 통과인데 효율성에서 시간초과
# def rotate(arr):
#     temp = deque([i for i in arr[0]])
#     for i in range(1,len(arr)-1):
#         temp.append(arr[i][-1])
#     temp += arr[-1][::-1]
#     for i in range(len(arr)-2,0,-1):
#         temp.append(arr[i][0])
#     c = temp.pop()
#     temp.appendleft(c)

#     for i in range(len(arr[0])):
#         item = temp.popleft()
#         arr[0][i] = item
#     for i in range(1,len(arr)-1):
#         item = temp.popleft()
#         arr[i][-1] = item
#     for i in range(len(arr[0])-1,-1,-1):
#         item = temp.popleft()
#         arr[-1][i] = item
#     for i in range(len(arr)-2,0,-1):
#         item = temp.popleft()
#         arr[i][0] = item
    
#     return arr

# def row(arr):
#     temp = arr.pop()
#     new_arr = [temp] + arr
#     return new_arr

# def solution(rc, op):
#     arr = rc
    
#     for i in op:
#         if i == 'Rotate':
#             arr = rotate(arr)
#         else:
#             arr = row(arr)
            
#     return arr



print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))