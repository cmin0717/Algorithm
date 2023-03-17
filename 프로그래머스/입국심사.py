def solution(n, times):
    start = 0
    end = n * max(times)
    
    while start <= end:
        mid = (start+end) // 2
        cnt = 0
        
        for i in times:
            cnt += mid//i
            
        if cnt < n:
            start = mid + 1
        else:
            end = mid - 1
            
    return start