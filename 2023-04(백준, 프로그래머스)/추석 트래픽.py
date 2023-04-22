def solution(lines):
    
    times = []
    
    for date in lines:
        # 주어진 문자열을 각 사용처에 맞게 편집
        day,time,rq = date.split(' ')
        h,m,s = time.split(':')
        s,ms = s.split('.')
        time = (int(h)*60*60 + int(m)*60 + int(s))*1000 + int(ms)
        rq = int(float(rq[:-1])*1000)

        # 만약 요청시간안에 날짜가 변한다면 그냥 0으로 넣어버린다.
        if time-rq+1 < 0:
            times.append([0,time])
        else:
            times.append([time-rq+1,time])
        
    result = 0
    
    for i in range(len(times)):
        cnt = 0
        start,end = times[i][1], times[i][1] + 1000
        # 각 요청마다 완탐으로 체크
        for j in range(len(times)):
            if start <= times[j][0] < end or start <= times[j][1] < end or times[j][0] <= start < times[j][1]:
                cnt += 1
        result = max(result, cnt)
    return result

solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])