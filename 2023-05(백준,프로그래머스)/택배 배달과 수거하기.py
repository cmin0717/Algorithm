def solution(cap, n, deliveries, pickups):
    
    result = [0] * n
    sd,sp = 0,0 # 누적합 사용
     # 각 집을 처리하려면 몇번째 트럭까지와야하는지 담는다.
    for i in range(n-1,-1,-1):
        if deliveries[i]:
            sd += deliveries[i]
            turn = sd//cap if sd % cap == 0 else (sd//cap) +1
            result[i] = turn # deliveries을 먼저 체크하기에 여기서는 max를 사용할필요가 없다.
        if pickups[i]:
            sp += pickups[i]
            turn = sp//cap if sp % cap == 0 else (sp//cap) +1
            result[i] = max(result[i], turn)

    # 그렇게 담은 트럭을 이용하여 최소로 움직일 거리를 구한다.
    cnt,idx = 0,0
    for i in range(n-1,-1,-1):
        t = result[i]
        if t > idx:
            cnt += (i+1)*2*(t-idx)
            idx = t # idx를 이용하여 중복 처리되는것을 방지
        
    return cnt