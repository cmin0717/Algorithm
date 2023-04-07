way = input()

nums = list(way.split('-')) # 빼기를 기준으로 나누어 준다. 그러면 0번째 인덱스 말고는 모조리 빼버리면 최저값이다.

result = sum(list(map(int,nums[0].split('+')))) # 빼기로 나눈 자료중에 0번째 인덱스만 더해준다.

for num in nums[1:]:
    result -= sum(list(map(int,num.split('+')))) # 나머지는 다 뺴주는데 안에 +도 있을수있으니 처리해주고 뺴준다.

print(result)

