num = int(input('정수를 입력해 주세요 : '))
breaker = 0 

if num > 1 :
    for i in range(1, 7):
        for j in range(1, num):
            if j**i == num and :
                print(str(j)+"**"+str(i))
                breaker = 1
                break
            else :
                continue
        if breaker == 1:
            break
else :
    print("2 이상의 정수를 입력해주세요.")