def solution(dartResult):
    
    num = []
    dic = {'S':1, 'D':2, 'T':3}
    check = ''
    
    for i in dartResult:
        
        if dic.get(i) != None:
            num.append(int(check)**dic[i])
            check = ''
        elif i in ['*', '#']:
            num.append(i)
        else:
            check += i
    
    result = []
    
    for i in num:
        if i == '*':
            if len(result) == 1:
                result[0] *= 2
            else:
                result[-1] *= 2
                result[-2] *= 2  
        elif i == '#':
            result[-1] = -result[-1]
        else:
            result.append(int(i))
    return sum(result)