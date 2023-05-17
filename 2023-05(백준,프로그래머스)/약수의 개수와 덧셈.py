def solution(left, right):
    # 약수을 구하는 함수
    def check(num):
        cnt = set()
        for i in range(1, round(num**0.5)+1):
            if num % i == 0:
                cnt.add(i)
                cnt.add(num // i)
        return len(cnt)
    
    result = 0
    for i in range(left, right+1):
        # 해당 숫자의 약수의 개수를 구한다.
        n = check(i)
        # result에 약수의 홀짝에 대해 알맞은 값을 더해준다.
        result += i if n % 2 == 0 else -i
    
    return result