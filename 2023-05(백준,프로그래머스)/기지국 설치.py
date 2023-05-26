def solution(n, stations, w):
    
    part = [] # 설치해야할 구간 저장
    start = 1

    # 현재 이미 세워진 기지국을 기준으로 새로 새워야할 구간을 구함
    for s in stations:
        part.append([start, s-(w+1)])
        start = s+(w+1)
    if start <= n:
        part.append([start, n])
    
    # 해당 구간 길이를 가지고 몇개 세워야하는지 판단
    result = 0
    for s,e in part:
        t = e-s+1
        r = (w*2)+1
        result += t // r if t % r == 0 else t //r +1
    
    return result