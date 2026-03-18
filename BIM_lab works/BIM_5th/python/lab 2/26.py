text=(input("Enter a string:"))
i=0
j=len(text)-1
flag=0
while i<j:
    if text[i]!=text[j]:
        flag=1
        break
    i+=1
    j-=1
if flag==0:
    print("palindrome")
else:
    print("not a palindrome")