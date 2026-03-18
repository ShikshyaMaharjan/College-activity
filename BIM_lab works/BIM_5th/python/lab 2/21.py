for i in range(1,300):
    temp=i
    sum=0
    digits=len(str(i))
    while temp>0:
        d=temp%10
        sum+=d**digits
        temp//=10
    if sum==i:
            print(i)