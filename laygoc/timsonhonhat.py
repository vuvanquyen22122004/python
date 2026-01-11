for x in range(int(input())):
    n =input()
    sum=0
    result=pow(10,9)
    for i in n:
        if i >='0' and i<='9':
            sum=sum*10+int(i);
        else:
            if sum != 0:
                result=min(result,sum)
            sum=0
    print(result)


