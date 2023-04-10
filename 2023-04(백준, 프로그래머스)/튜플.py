def solution(s):
    w = [[]]
    s = sorted(s[2:-2].split('},{'), key=lambda x: len(x))
    check = set()
    result = []
    
    for i in s:
        i = i.split(',')
        for j in i:
            if j not in check:
                result.append(int(j))
                check.add(j)
                
    return result