def solution(fees, records):
    
    dic = {} # 각 자동차의 누적 주차시간을 저장
    
    for record in records:
        time,num,state = record.split()
        h,m = time.split(':')
        time = int(h) * 60 + int(m)
        dic.setdefault(num,[])
        dic[num].append(time) # 주어진 이용 내역을 보고 해당 번호의 자동차에 시간을 넣는다.

    for i in dic.keys():
        if len(dic[i]) % 2 != 0: # 주어진 시간이 홀수면 제일 늦게 나가는시간인 23:59분을 넣어준다.
            dic[i].append(1439)
        tt = 0
        for j in range(0,len(dic[i]),2): # 각 시간을 2개씩 나누너 값의 차를 합해 해당 자동차에 넣어준다.
            tt += dic[i][j+1] - dic[i][j]
        dic[i] = tt - fees[0]

    result = []
    for k in sorted(dic.keys()): # 위에서 구한 누적 주차시간을 통해 주차요금 계산
        if dic[k] <= 0:
            result.append(fees[1])
            continue
        div,mod = divmod(dic[k], fees[2])
        pay = (div+1)*fees[3] if mod != 0 else div*fees[3]
        result.append(fees[1] + pay)
    return result