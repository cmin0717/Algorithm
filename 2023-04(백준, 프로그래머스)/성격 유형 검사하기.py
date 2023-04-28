def solution(survey, choices):
    point = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    dic = {}
    
    for x,y in ['R','T'],['C','F'],['J','M'],['A','N']: # 미리 dic형태로 넣어둔다.
        dic.setdefault(x,0)
        dic.setdefault(y,0)
    
    # 4점 이상이면 우측 문자에 이하면 좌측 문자에
    for i in range(len(survey)):
        c = [w for w in survey[i]]     
        if choices[i] < 4:
            dic[c[0]] += point[choices[i]]
        else:
            dic[c[1]] += point[choices[i]]
    
    # 점수를 1기준으로 같다면 문자열을 기준으로 정렬
    result = ''
    for x,y in ['R','T'],['C','F'],['J','M'],['A','N']:
        find = sorted([[x,dic[x]],[y,dic[y]]], key=lambda x: (-x[1],x[0]))
        result += find[0][0]
        
    return result