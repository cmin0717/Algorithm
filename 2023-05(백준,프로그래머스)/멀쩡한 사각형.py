def solution(w,h):
    # 최대 공약수 구하기
    def gcd(x,y):
        while y:
            x,y = y, x%y
        return x
    n = gcd(max(w,h), min(w,h))

    # 최대 박스 수
    total = w*h
    # 해당 공약수에 해당하는 박스 수
    s_box = w//n + h//n -1

    return total - s_box*n