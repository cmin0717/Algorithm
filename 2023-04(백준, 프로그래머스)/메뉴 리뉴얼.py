from itertools import combinations

def solution(orders, course):
    food = {}
    for order in orders:
        order = sorted(list(order)) # 동일한 조건을 주기위해 정렬하고 시작한다.
        for c in course:
            food.setdefault(c,{}) 
            for i in combinations(order,c): # 각 문자열에서 course만큼 조합을 뽑는다.
                food[c].setdefault(''.join(i),0)
                food[c][''.join(i)] += 1

    result = []
    
    for c in course:
        if food[c].values():
            max_c = max(food[c].values()) # 모아온 딕셔너리에서 최대값 가져온다.
            if max_c < 2: continue
            for k,v in food[c].items():
                if v == max_c: # 해당 키의 벨류가 최대값과 같다면 추가
                    result.append(k)
    return sorted(result)
    