def solution(q1, q2):
    
    s1, s2 = sum(q1), sum(q2) # 각 큐의 합을 저장
    x,y,l = 0,0,len(q1) 
    
    while x < l*2 and y < l*2 and s1 != s2: # 조건 생성
        if s1 < s2:
            s1 += q2[y]
            s2 -= q2[y]
            q1.append(q2[y])
            y += 1
        else:
            s1 -= q1[x]
            s2 += q1[x]
            q2.append(q1[x])
            x += 1
            
    return x+y if x+y < l*3 else -1 # 최대 진행할수있는 횟수는 l*3번까지이다.



solution([3, 3, 3, 3], [3, 3, 21, 3])