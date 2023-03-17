def solution(number, k):
    nums = [i for i in number]
    idx = 0
    result = ''

    while len(result) != len(number) - k:
        if nums[idx] == '9':
            idx += 1
            result += '9'
            continue

        for i in range(1,k+1):
            if nums[idx] < nums[idx+i]:
                idx = idx+i
                k -= i
                break
        else:
            result += nums[idx]
            idx += 1

        if k == 0:
            for i in nums[idx:]:
                result += i
            break
    
    return result

print(solution('4177252841',4))