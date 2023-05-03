def solution(n, k):
    
    # num에 10진수를 k진수로 변환한 값을 담는다.
    num = ''
    while n != 0:
        div,mod = divmod(n,k)
        num += str(mod)
        n = div
    
    # 역순으로 담겨있기에 역순으로 정렬
    nums = num[::-1].split('0')
    
    # 에라토스테네스의 체를 사용하여 빠르게 소수 판별
    result = 0
    for i in nums:
        if i == '1' or not i: continue
        if i in ['2','3']:
            result += 1
            continue
        for j in range(2,round(int(i)**0.5)+1):
            if int(i) % j == 0:
                break
        else:
            result += 1
            
    return result