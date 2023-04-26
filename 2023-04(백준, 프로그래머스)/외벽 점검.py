from itertools import permutations

def solution(n, weaks, dist):
    
    result = float('inf')
    weak = weaks + [w+n for w in weaks]
    w_l = len(weaks)

    for i in range(len(weaks)): # 시작 위치 정하기
        w = weaks[i]
        for fs in permutations(dist): # 조합뽑기
            cnt, now = 1, w
            for f in fs: # 받아온 조합을 하나씩 배치해가며 조건 판단
                now += f
                if now < weak[i+w_l-1]: # 현재 위치가 모든 취약점을 넘어섰다면 종료 아니라면 계속 진행
                    cnt += 1
                    for wk in weak[i+1:]:
                        if wk > now:
                            now = wk
                            break
                else:
                    result = min(result, cnt)
                    break

    return result if result != float('inf') else -1


solution(12, [1, 5, 6, 10], [1, 2, 3, 4])