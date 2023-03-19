from itertools import *

def check(n):
    for i in range(2, round(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    nums = [i for i in numbers]
    cnt = 0
    dic = {0:1, 1:1} # 0,1은 소수로 판단할수없기에 미리 넣어둔다.
    for i in range(1, len(nums)+1):
        for j in permutations(nums,i):
            new_num = int(''.join(j))
            if dic.get(new_num) == None:
                dic[new_num] = 1
                if check(new_num): cnt += 1
    return cnt

print(solution("011"))