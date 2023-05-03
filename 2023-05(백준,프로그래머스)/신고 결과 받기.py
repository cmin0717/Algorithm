def solution(id_list, report, k):
    
    dic = {} # 주어진 id를 미리 딕셔너리에 넣어둔다.
    for id in id_list:
        dic.setdefault(id,[0,set()])
    
    # 신고 내역을 통해 신고자에는 신고하는사람 아이디를 저장 신고당한자는 당한 횟수 +1
    for r in report:
        u,bu = r.split()
        if bu not in dic[u][1]:
            dic[bu][0] += 1
            dic[u][1].add(bu)
    
    # 주어진 신고횟수를 초과한 id는 밴아이디에 추가
    ban_id = set()
    for key in dic.keys():
        if dic[key][0] >= k:
            ban_id.add(key)
    
    # 각 아이디를 돌면서 내가 신고한 아이디가 밴아이디에서 체크후 결과에 저장
    result = []
    for id in id_list:
        cnt = 0
        for b in dic[id][1]:
            if b in ban_id:
                cnt += 1
        result.append(cnt)
        
    return result