num=int (input("Enter a number:"))
i=2
print(num,"is")
while i<=num//2:
    if num%i==0:
        print("nto prime number")
        break
    i+=1
else:
    if num>1:
        print("prime number")
    else:
        print("not prime number")