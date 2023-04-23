def solution(N, stages):
    # stage에 도달했지만 실패한사람, stage에 도달한사람, stage
    stage = [[0,0,i] for i in range(N+1)]
    
    for i in stages:
        # 마지막 스테이지까지 깬사람이니깐 stage도달한 사람에만 +1
        if i == N+1:
            stage[N][1] += 1
        # stage에 도달했지만 깨지 못한거니 둘다 +1
        else:
            stage[i][1] += 1
            stage[i][0] += 1
    # 현재 스테이지까지 왔다는건 나머지 아래 스테이지는 도달한거니깐 위에서 부터 아래로 더해간ㄷㅏ.
    for i in range(N,0,-1):
        stage[i-1][1] += stage[i][1]
    
    # 실패율과 stage번호를 출력
    for i in range(1,N+1):
        fail = 0 if stage[i][1] == 0 else stage[i][0] / stage[i][1]
        stage[i] = [fail,i]
    stage = sorted(stage[1:],key=lambda x:(-x[0],x[1]))
    
    return [i[1] for i in stage]