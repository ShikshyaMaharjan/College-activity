num=int(input("Enter a number:"))
temp=num
sum=0
digits=len(str(num))
while temp>0:
    digits=temp%10
    sum+=digits*digits*digits
    temp//=10
if sum==num:
    print("Armstrong number")
else:
    print("Not Armstrong number")

