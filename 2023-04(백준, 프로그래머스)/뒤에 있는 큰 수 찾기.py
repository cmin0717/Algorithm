def solution(nums):
    result = [0] * len(nums)
    
    check = [[nums[0],0]] # 값과 idx를 저장
    
    for i in range(1,len(nums)):
        for _ in range(len(check)-1,-1,-1):
            if check[-1][0] >= nums[i]: # 현재값보다 크다면 스텍에 저장
                check.append([nums[i],i])
                break
            else:
                # 작다면 스텍에서 pop시키고 해당값을 result에 넣어준다.
                c = check.pop()
                result[c[1]] = nums[i]
        else:
            # break문을 만나지 않고 종료시 스텍에 저장
            check.append([nums[i],i])
    
    # 다 끝나고도 스텍에 남아있는 애들은 뒷 큰수가 없는 친구들이니깐 -1 저장
    for x,y in check:
        result[y] = -1
    return result


# 딕셔너리를 사용한 dp방식으로 풀이했는데 테케 21번에서 막힘(5 4 3 2 1 1 2 3 4 5 이런 형태에서는 시간초과나는듯)
# def solution(nums):
#     dic = {}
#     result = []
#     for i in range(len(nums)-1):
#         if dic.get(nums[i]) != None:
#             if dic[nums[i]][-1][1] > i:
#                 result.append(dic[nums[i]][-1][0])
#                 continue
#         else:
#             dic[nums[i]] = []

#         for j in range(i+1, len(nums)):
#             if nums[i] < nums[j]:
#                 dic[nums[i]].append([nums[j], j])
#                 result.append(nums[j])
#                 break
#         else:
#             dic[nums[i]].append([-1,1000001])
#             result.append(-1)
    
#     return result + [-1]