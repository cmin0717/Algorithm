def solution(gems):
    dic = {gems[0]:1}
    gems_size = len(set(gems))
    result = [1,100000]
    l,r = 0,0
    
    while l < len(gems) and r < len(gems): # 각 포인터가 범위를 넘어가면 종료    
        if len(dic) == gems_size: # 현재 모든 보석이 모였다면
            if result[1]-result[0] > r-l:
                result = [l+1,r+1]
            dic[gems[l]] -= 1 # 보석이 다 모였으니 left를 하나씩 줄여간다.
            if dic[gems[l]] == 0:
                del dic[gems[l]] # 만일 보석의 개수가 0이 된다면 dic에서 지워준다.
            l += 1
        else:
            # 보석을 다 모으지 못했다면 right를 하나씩 늘려간다.
            r += 1
            if r == len(gems):break # 인덱스 오류를 막기위해
            if dic.get(gems[r]) == None:
                dic[gems[r]] = 1
            else:
                dic[gems[r]] += 1
                
    return result
solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])