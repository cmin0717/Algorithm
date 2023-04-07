def solution(score):
    x,y = score[0][0], score[0][1] # target의 점수는 미리 저장시킨다.
    scores = sorted(score[1:], key=lambda x: (x[0],-x[1])) # 근무태도는 내림차순으로 동료평가는 오름차순으로 정렬
    
    result = 1
    cnt = 0
    
    if len(scores) != 0:
        check = scores[-1][1] # 근무태도 점수가 가장 높은 사람의 동료평가를 디폴트값으로 설정
    
    for a,b in scores[::-1]: # range를 이용해서 뒤에서 오는것보다 이게 더빠르다 이유는 잘모르겠다.
        
        if b < check and a+b > x+y: # a는 내림차순으로 했기에 무조건 같거나 작다. 타겟보다 높은 점수만 확인하면 된다.
            cnt += 1
        else:
            check = max(check, b) # a는 무조건 같거나 작기에 check값은 항상 큰값으로 유지해야한다.
            
        if x < a and y < b:
            return -1
        
        if a+b > x+y:
            result += 1
        
    return result - cnt

solution([[2, 2], [2, 2], [2, 3], [3, 2]])