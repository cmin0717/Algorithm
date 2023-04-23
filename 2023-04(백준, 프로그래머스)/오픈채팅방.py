def solution(record):
    
    memory = [] # 각 유효한 명령어를 모아둔다.
    dic ={} # 유저의 닉네임을 저장
    
    for i in record:
        info = i.split(' ')
        
        if info[0] != 'Leave': # 나가는것이 아니라면 주어진 닉네임으로 변경
            dic[info[1]] = info[2]
        
        if info[0] == 'Change': # 변경은 명령어에 저장하지 않는다 어차피 위에서 변경하였기에
            continue
            
        memory.append([info[0],info[1]])
    
    result = []
    
    for tp,user in memory: # 각 명령어에 따라 메시지 출력
        if tp == 'Enter':
            result.append(f"{dic[user]}님이 들어왔습니다.")
        else:
            result.append(f"{dic[user]}님이 나갔습니다.")
    
    return result