def solution(n, t, m, p):
    
    check = '0'
    result = ''
    dic = {'10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}
    cnt = 1
    
    # N진수로 변환해주는 함수
    def n_trans(cnt, n):
        num = ''
        
        while cnt > 0:
            mod = cnt % n # n진수로 변환한다는건 나머지를 모아가는것
            cnt = cnt // n # 다음 수로는 n으로 나눈 몫을 전달
            
            num += str(mod) if mod < 10 else dic[str(mod)]
        
        return num[::-1] # 진수로 표현하려면 역순으로 전달해주어야한다.
    
    while len(check) < t * m:
        check += n_trans(cnt, n)
        cnt += 1
    
    for i in range(p-1, len(check[:t*m]), m): # 얻어낸 연속된 문자에서 p순서에 해당하는 자리만 더해준다.
        result += check[i]
    
    return result
solution(16, 16, 2, 1)
# 당연히 2,8,16진수로만 변환하는줄 알아서 쫌 삽질했다...