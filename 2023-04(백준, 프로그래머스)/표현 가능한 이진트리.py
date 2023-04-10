import math

# 이진 포화트리이니깐 트리의 빈공간을 더미 노드(0)으로 채워준다.
def trans(n):
    num = bin(n)[2:]
    d = 2 ** (int(math.log2(len(num)))+1) -1
    num = '0'*(d-len(num)) + str(num)
    return num

def check(num,tf):
    mid = len(num) // 2
    if len(num) == 0:
        return True

    new_tf = (num[mid] == '1') # 현재의 노드의 값을 저장
    
    if new_tf and not tf: # 현재 노드는 1인데 부모가 0이라면 규칙에서 위반되므로 false리턴
        return False
    else:
        return check(num[:mid], new_tf) and check(num[mid+1:],new_tf) # 이런 방식으로 모든 트리의 노드들이 true를 반환하면 true아니라면 false 리턴

def solution(nums):
    result = []
    for i in nums:
        n = trans(i)
        if n[len(n)//2] == '0' or not check(n,True): # 둘중하나라도 만족하면 조건이 성립되지 않았으므로 0저장
            result.append(0)
        else:
            result.append(1)

    return result
solution([63, 111, 95])