def solution(prices):
    result = []
    for i in range(len(prices)):
        day = 0
        for j in range(i+1,len(prices)):
            day += 1
            if prices[i] <= prices[j]:
                continue
            else:
                result.append(day)
                break
        else:
            result.append(day)
            
    return result