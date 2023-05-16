def solution(a, b, g, s, w, t):
    # 시작점은 제일 작은 0부터, 끝점은 시간이 제일 오래걸리는 트럭이 1씩 옮긴다고 가정
    start, end = 0, (a+b) * (max(t)*2)
    
    # 이분탐색
    while start <= end:
        mid = (start + end) // 2
        now_a, now_b, total = 0, 0, 0
        
        for i in range(len(t)):
            # mid값을 통해 트럭이 최대 몇번 왔다갔다하는지 구함
            d,m = divmod(mid, t[i]*2)
            if m >= t[i]:
                d += 1
            # 트럭이 해당 시간에 최대 몇kg을 옮기는지 저장
            rest = w[i]*d

            # 골드를 옮길수있는 최대양(옮기는 무게, 보유하는 무게중 작은값을 선택해야한다. 없는걸 옮길순 없응꼐)            
            now_a += min(rest, g[i])
            # 실버
            now_b += min(rest, s[i])
            # 위와 같이 구하면 한번 갈때 2번가는것처럼 더해진다.
            # 그래서 실제 옮기는 무게를 total에 담아 준다.
            total += min(rest, g[i] + s[i])
        
        # 3가지 조건을 만족하면 넉넉한 시간이니깐 시간 단축
        if now_a >= a and now_b >= b and total >= a+b:
            end = mid - 1
        # 아니라면 부족한 시간이니 시간 증가
        else:
            start = mid + 1
    
    return start