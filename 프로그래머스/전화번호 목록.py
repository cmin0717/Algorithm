def solution(pb):
    pb.sort()
    for i in range(len(pb)-1):
        min_len = min(len(pb[i]), len(pb[i+1]))
        if pb[i][:min_len] == pb[i+1][:min_len]:
            return False
    else:
        return True
# 숫자문자열의 정렬은 문자열의 len 기준이 아닌 숫자문자열 앞에서 부터 작은 값으로 정렬된다.