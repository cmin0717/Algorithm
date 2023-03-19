def solution(g, p):
    music = {}
    
    for i in range(len(g)):
        if music.get(g[i]) == None:
            music[g[i]] = [p[i],[p[i],i]]
        else:
            music[g[i]][0] += p[i]
            music[g[i]].append([p[i],i])
            
    k_v = sorted([[music[i][0],i] for i in music.keys()], reverse=True)
    
    result = []
    for total,key in k_v:
        n = sorted(music[key][1:],key=lambda x:(-x[0],x[1])) # lambda로 정렬 기준을 잡을때 -을 하면 내림차순
        for i in range(len(n)):                              # 위와 같이 x:(-x[0],[1])이라면 0번째는 내림하고 1번쨰는 올림으로 정렬
            if i == 2 : break
            result.append(n[i][1])

    return result