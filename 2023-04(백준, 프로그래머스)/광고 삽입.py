def solution(play_time, adv_time, logs):
    logs = [[play_time,adv_time]] + [l.split('-') for l in logs]
    
    for i in range(len(logs)):
        s,e = logs[i][0].split(':'), logs[i][1].split(':')
        logs[i][0] = int(s[0]) * 3600 + int(s[1]) *60 + int(s[2])
        logs[i][1] = int(e[0]) * 3600 + int(e[1]) *60 + int(e[2]) # 모든 시간을 초 단위로 변환
    
    pt, at, logs = logs[0][0],logs[0][1],logs[1:]

    check = [0] * (pt+1) # 총 재생시간만큼 배열 생성

    for s,e in logs:
        check[s] += 1 # 시작과 끝에 값을 더해줌 누적합사용
        check[e] -= 1
    
    # 누적합 적용
    for i in range(1,pt+1):
        check[i] += check[i-1]
    # 누적합에 누적합 적용
    for i in range(1,pt+1):
        check[i] += check[i-1]
    
    num = [0,0]
    # 0부터 하나씩 다해서 제일 큰값만 남긴다.
    for i in range(at-1,pt):
        if i <= at:
            if check[i] > num[0]:
                num = [check[i],i-at+1]
        else:
            sum_num = check[i] - check[i-at]
            if sum_num > num[0]:
                num = [sum_num,i-at+1]
    
    num = num[1]
    result = ''
    # 해당 값을 숫자에서 시간으로 변경후 출력
    for i in [3600,60]:
        div,mod = divmod(num,i)
        if len(str(div)) == 1:
            result += '0'
        result += str(div)+':'
        num = mod
         
    if len(str(num)) == 1:
        result += '0'
    result += str(num)
    
    return result
    