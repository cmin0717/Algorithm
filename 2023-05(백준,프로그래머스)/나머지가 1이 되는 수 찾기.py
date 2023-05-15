def solution(n):
    num = n-1
    
    result = []
    for i in range(1,round(n**0.5)+1):
        if num % i == 0:
            result.append(i)
            result.append(num // i)
    
    # 1을 제외한 몫중 가장 작은값 리턴
    return min(result[1:])