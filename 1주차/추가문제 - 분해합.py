n = int(input())

for i in range(n-(len(str(n)) * 10),n+1): # 각 자리에 최대 9가 올수있다, 결국 몇자리수 * 9부터 n까지만 확인하면 된다.

    str_num = str(abs(i)) # 1의 자리의 수가 주어질 경우도 있기에 절대값으로 커버했다. 귀찬아서
    slice_num = [int(j) for j in str_num] # 각 자리수를 인트화

    if i + sum(slice_num) == n:
        print(i)
        break
else:
    print(0)

