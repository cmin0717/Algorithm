def solution(today, terms, p):
    kinds = {}
    for i in terms:
        kind, term = i.split(' ')
        kinds[kind] = int(term)
        
    ty,tm,td = map(int, today.split('.'))
    result =[]
    for i in range(len(p)):
        day, k = p[i].split(' ')
        y,m,d = map(int, day.split('.'))
        m += kinds[k]
        y += (m-1) // 12
        m = ((m-1) % 12) + 1
        
        if ty > y:
            result.append(i+1)
        elif ty == y and tm > m:
            result.append(i+1)
        elif ty == y and tm == m and td >= d:
            result.append(i+1)
    return result
        
        