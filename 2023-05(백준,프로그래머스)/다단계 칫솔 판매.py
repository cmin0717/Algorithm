def solution(enroll, referral, seller, amount):
    link = [[] for _ in range(len(enroll)+1)] # 각 연결된 사람끼리 링크드 리스트 형성
    dic = {}

    # 해당 인원의 idx와 순이익을 딕셔너리에 담는다.
    for i in range(1,len(enroll)+1):
        dic[enroll[i-1]] = [i,0]
    
    # 링크드 리스트 작업 상위가 센터라면 0을 삽입
    for i in range(len(referral)):
        if referral[i] == '-':
            link[dic[enroll[i]][0]].append(0)
        else:
            link[dic[enroll[i]][0]].append(dic[referral[i]][0])

    # 각 물건 판매시 이익분배 시작
    for i in range(len(seller)):
        name = seller[i]
        p_name = enroll[link[dic[name][0]][0]-1] if link[dic[name][0]][0] != 0 else False
        t = int((100 * amount[i]) * 0.1)

        dic[name][1] += (100 * amount[i]) - t

        if p_name:
            p_idx = link[dic[name][0]][0]-1 # 상위 맴버의 인덱스
            while t >= 1 and p_idx >= 0: # 넘겨줄 돈이 충분하거나 최상위 맴버가 아니라면
                p_name = enroll[p_idx]
                new_t = int(t*0.1)
                dic[p_name][1] += t if new_t < 1 else t-new_t
                t = new_t
                p_idx = link[dic[p_name][0]][0]-1 # 다음 상위 맴버의 인덱스를 담아준다.
    
    return [cost for idx,cost in dic.values()]

# 처음에 문제를 잘못봐서 위상정렬로 풀어야하는줄 알았는데 막상보니깐 물건 판매시 마다 작업을 해주는것이었다....
# 또한 10퍼센트라는 말이 너무 애매모호하게 문제에서 알려줘서 반올림을 사용했는데 거기서 막혔다.
# 문제 설명이 쫌 그렇네....
        