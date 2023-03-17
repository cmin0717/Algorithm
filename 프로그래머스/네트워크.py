def solution(n, pc):
    result = [i for i in range(n)]
    
    def check(arr,idx):
        for i in range(n):
            if i == idx: continue
            if arr[idx][i] == 1 and result[i] != result[idx] :
                result[i] = result[idx]
                check(arr,i)
                
    for i in range(n):
        if result[i] == i:
            check(pc,i)
            
    return len(set(result))

# 아..함수형 제출 헷갈린다