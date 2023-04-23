from itertools import combinations

def solution(relation):
    
    result = [] # 유효키 리스트
    s = [i for i in range(len(relation[0]))] # 콤비네이션을 사용하기 위해 인덱스 리스트 구성
    
    for idx in range(len(s)): # 콤비네이션으로 1~n개 까지 뽑기위해
        for com in combinations(s,idx+1): # 콤비네이션을 사용하여 조합을 뽑는다.
            check = set()
            visit = [i for i in com] # 현재 조합에서 방문해야할 인덱스를 출력
            temp = True

            for c in result: # 유효키 리스트를 가져와 현재 조합이 최소성을 만족하는지 판단
                cnt = 0
                for cc in c:
                    if cc in visit:
                        cnt += 1
                if cnt == len(c):
                    temp = False
                    break

            if temp: # 최소성을 만족한다면 현재 조합키가 유효키가 될수있는지 판다
                for r in relation:
                    key = ''
                    for z in com:
                        key += r[z]+'-'
                    check.add(key)
                if len(check) == len(relation): # 유효성을 보장한다면 유효키 리스트에 키구성리스트를 추가
                    result.append(visit)
                    
    return len(result) # 유효키리스트의 길이를 리턴

solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]])