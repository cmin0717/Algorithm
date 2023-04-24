def solution(time, k):
    
    idx = 0
    time = [[time[i],i+1] for i in range(len(time))] # 음식에 idx를 추가하여 몇번째 음식인지 확인
    
    while k > 0 and time: # 횟수가 남아있고 먹을 음식이 남아있다면
        div,mod = divmod(k,len(time))
        new_time = []
        
        if div == 0: #몫이 없다면 나머지를 idx에 더하고 종료
            idx += mod
            break
        
        for t,i in time:
            if t - div > 0:
                new_time.append([t-div,i]) # 음식이 남는다면 저장
            else:
                mod += abs(t-div) # 시간이 남는다면 저장
        time = new_time
        k = mod
    
    return time[idx][1] if len(time) else -1