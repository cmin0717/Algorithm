from heapq import *

def solution(jobs):
    jobs.sort()
    job = [[y,x] for x,y in jobs[1:]]
    heapify(job)
    
    now = sum(jobs[0])
    result = now-jobs[0][0]
    check = []
    
    while job or check:
        if len(job) == 0 and check:
            min_start = 1001
            for i in range(len(job)):
                min_start = min(min_start, job[i][1])
            for _ in range(len(check)):
                m = check.pop()
                heappush(job,m)
                min_start = min(min_start,m[1])
            now = min_start
            
        while job:
            time,start = heappop(job)
            if start > now:
                check.append([time,start])
                continue
            now += time
            result += now-start
            for _ in range(len(check)):
                heappush(job,check.pop())
            
    return result // len(jobs)

print(solution([[3,10],[20,50]]))