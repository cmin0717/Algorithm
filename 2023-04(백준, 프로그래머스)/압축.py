def solution(msg):    
    words, now, cnt, idx = {}, '', 27, 0 # 단어를 모아둘 딕셔너리, 현재 문자, 다음 저장될 문자의 번호, 현재 인덱스
    result = []
    msg += ' ' # 마지막 문자를 처리하기 위해 인덱스 범위를 하나 늘려주었다.
    
    for i in range(65,91):
        words[chr(i)] = i-64
        
    while idx < len(msg)-1: # 패딩문자가 하나들어갔기에 -1
        now += msg[idx]
        
        if words.get(now+msg[idx+1]) != None: # 해당문자가 있다면 idx +1해주고 컨티뉴
            idx += 1
            continue
        else:
            result.append(words[now]) # 해당문자가 없다면 추가해준다.
            words[now+msg[idx+1]] = cnt
            cnt += 1
            now = ''
            idx += 1
    
    return result