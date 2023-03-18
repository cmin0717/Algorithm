def solution(n):
    c = {}
    for value,key in n:
        if c.get(key) == None:
            c[key] = [value]
        else:
            c[key].append(value)
            
    c_time = [len(c[i]) for i in c.keys()]    
    cnt = 1
    
    # 옷의 경우의수를 방정식으로 정리하면 (1+a)(1+b)..(1+n) -1 이 된다.
    for i in c_time:
        cnt *= i+1
            
    return cnt-1



# 너무 코드적으로만 접근하였다. 단순한 방정식으로 해결가능한 문제였는데...
# 아래는 조합으로 풀려고 한 실패 코드

# from itertools import combinations
# def solution(n):
#     c = {}
#     for value,key in n:
#         if c.get(key) == None:
#             c[key] = [value]
#         else:
#             c[key].append(value)
            
#     c_time = [len(c[i]) for i in c.keys()]    
#     cnt = 0
    
#     for i in range(1,len(c_time)+1):
#         for j in combinations(c_time,i):
#             check = 1
#             for a in j:
#                 check *= a
#             cnt += check
            
#     return cnt