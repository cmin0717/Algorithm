def solution(n, left, right):
    
    result = []
    
    for i in range(left, right+1):
        # 행과 열은 몫과 나머지이다.
        x,y = divmod(i,n)
        # 문제 조건에 따라 행과 열중 큰값을 넣어주면 된다.
        result.append(max([x,y])+1)

    return result

