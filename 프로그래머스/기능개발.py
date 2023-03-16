import math

def solution(p, s):
    days = [math.ceil((100-p[i]) / s[i]) for i in range(len(p))]
    result,check,cnt,idx = [],1,1,0
    
    while sum(result) != len(days):
        if idx+check < len(days) and days[idx] >= days[idx+check]:
            check += 1
            cnt += 1
        else:
            result.append(cnt)
            cnt = 1
            idx = idx+check
            check = 1

    return result

print(solution(	[95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))