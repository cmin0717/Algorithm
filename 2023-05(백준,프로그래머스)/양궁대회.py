def solution(n, info):
    score = [i for i in range(11) if info[i]] # 현재 도전자가 맞힌과녁을 구한다.
    state = [i+1 for i in info] # 챔피언이 해당과녁을 맞추려면 쏴야하는 화살수를 구한다.
    result = []
    
    # 완탐으로 탐색
    def find(idx):
        
        total = sum([state[i] for i in idx]) # 현재까지 쏜 화살수
        a = sum([10-i for i in score if i not in idx]) # 현재 도전자의 점수
        b = sum([10-i for i in idx]) # 현재 챔피언의 점수
        
        if b > a and total <= n: # 챔피언의 점수가 도전자보다 높고 화살수도 적당하다면 저장
            result.append([b-a,idx])

        for i in range(idx[-1]+1,11): # 조건을 만족하면 다음 과녁들로 이동
            if total+state[i] <= n:
                find(idx+[i])
                
    for idx in range(11): # 출발점을 하나씩 돌린다.
        find([idx])

    if not result: return [-1] # 챔피언이 한번도 도전자를 넘지못했으면 -1 리턴

    # 챔피언과 도전자의 점수차이가 가장큰애들만 남긴다.
    max_score = max([r[0] for r in result])
    result = [r[1] for r in result if r[0] == max_score]
    
    # 화살을 부족하게 쏜애들은 0점과녁으로 남은 화살을 올인
    for i in range(len(result)):
        r = [state[j] if j in result[i] else 0 for j in range(11)]
        if sum(r) < n:
            r[-1] += n-sum(r)
        result[i] = r
    # 기준을 뒤에서 부터 내림차순으로 정렬
    result.sort(key=lambda x:x[::-1] ,reverse=True)
    return result[0]

solution(3, [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0])
