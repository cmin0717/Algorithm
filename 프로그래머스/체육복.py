def solution(n, lost, reserve):
    n_lost,n_reserve,check = [],[],[]
    n_reserve = [i for i in reserve if i not in lost]
    n_lost = [i for i in lost if i not in reserve]
    
    n_lost.sort()
    for i in n_lost:
        if i-1 not in check and i-1 in n_reserve:
            check.append(i-1)
            continue
        if i+1 not in check and i+1 in n_reserve:
            check.append(i+1)
            continue
        n -= 1
    return n

print(solution(5,[2,3,4],[1,3,5]))