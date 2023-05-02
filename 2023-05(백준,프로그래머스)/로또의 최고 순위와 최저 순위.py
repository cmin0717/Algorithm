def solution(lottos, win_nums):
    
    dic = {6:1,5:2,4:3,3:4,2:5} # 각 점수별로 등수를 딕셔너리에 담는다.
    cnt,zero_cnt = 0,0 
    
    for n in lottos:
        if n != 0 and n in win_nums:
            cnt += 1
        if n == 0:
            zero_cnt += 1
            
    mn,mx = cnt, cnt+zero_cnt
    result = []
    
    # 해당 값이 점수판에 있다면 꺼내서 담고 없다면 꼴등인 6을 넣는다.
    for i in mx,mn:
        if i in dic:
            result.append(dic[i])
        else:
            result.append(6)
    return result