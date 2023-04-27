import itertools

def solution(infos, querys):
    
    dic = {}
    
    for info in infos:
        info = info.split()
        binarys = list(itertools.product((True, False), repeat=4)) # 각 info에서 -를 넣을수있는 경우만큼 dic에 넣어준다.
        for b in binarys:
            word = ''.join([info[i] if b[i] else '-' for i in range(4)])
            dic.setdefault(word,[])
            dic[word].append(int(info[-1]))
    
    # 아래서 같은걸 여러번 정렬할수있으니 미리 한번에 정렬한다.
    for k in dic.keys():
        dic[k].sort()

    result = []
    for query in querys:
        a,_,b,_,c,_,d,e = query.split()
        e = int(e)
        
        # 값이 없는 애들은 0을 바로 넣어준다.
        word = ''.join([a,b,c,d])
        if word not in dic:
            result.append(0)
            continue
        
        # 이분탐색을 이용하여 주어진 값보다 큰애들의 수를 알아낸다.
        start,end = 0,len(dic[word])-1
        while start <= end:
            mid = (start+end) // 2
            if dic[word][mid] < e:
                start = mid+1
            else:
                end = mid-1
        
        result.append(len(dic[word]) - start)
    return result