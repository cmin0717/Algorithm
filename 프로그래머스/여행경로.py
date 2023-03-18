def solution(tk):
    link = {}
    for s,e in tk:
        if link.get(s) == None:
            link[s] = [e]
        else:
            link[s].append(e)
    
    for i in link.keys():
        link[i] = sorted(link[i])
        
    total = len(tk)+1
    result = []
    
    def check(arr,start, time, visit):
        if len(visit) == total:
            result.append(visit)
            return
        
        if arr.get(start) != None and len(arr[start]) != 0:
            for i in range(len(arr[start])):
                name = arr[start].pop(i)
                check(arr, name, time+1, visit + [name])
                arr[start].append(name)
                arr[start].sort()
        

    check(link,'ICN',0,['ICN']) # 무조건 인천 출발을 못봤다....스벌

    return result[0]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))