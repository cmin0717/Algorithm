from collections import deque

def solution(cacheSize, city):
    cache = deque([])
    city = [i.upper() for i in city] # 대소문자를 통일시켜주기 위해
    total_time = 0
    start = 0
    
    if cacheSize != 0: # cachesize가 0일때 예외처리해주기위해
        cache.append(city[0])
        total_time += 5
        start = 1
    
    for i in range(start,len(city)):
        
        if city[i] in cache and len(cache) != 0:
            total_time += 1
            cache.remove(city[i]) # 히트가 된다면 원래 cache에 있던걸 맨뒤로 옮겨주어야한다.
        else:
            total_time += 5
            if cache and len(cache) == cacheSize: cache.popleft()
        
        if len(cache) < cacheSize: # cache의 자리가 있다면 넣어준다.
            cache.append(city[i])
    
    return total_time
solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])