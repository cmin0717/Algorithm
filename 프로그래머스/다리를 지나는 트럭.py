from collections import deque

def solution(bl, bw, tw):
    b = deque([])
    end = []
    truck = deque(tw)
    time = 1
    
    while len(end) != len(tw):
        if len(b) != 0 and b[0][0] + bl == time:
            end.append(b.popleft()[1])
        if len(truck) != 0 and sum([i[1] for i in b]) + truck[0] <= bw:
            t = truck.popleft()
            b.append([time,t])
        time += 1
    
    return time-1

solution(2,10,[7,4,5,6])