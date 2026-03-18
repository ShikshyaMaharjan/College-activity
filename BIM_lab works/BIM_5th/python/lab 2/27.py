s1=input("Enter a first string:").replace(" ","").lower()
s2=input("Enter a second string:").replace(" ","").lower()
if len(s1)!= len(s2):
    print("not anagram strings")
else:
    i=0
    anagram=True
    while i<len(s1):
        count1=0
        count2=0
        j=0
        while j< len(s1):
            if s1[j]==s1[i]:
                count1+=1
            if s2[j]==s1[i]:
                count2+=1
            j+=1
        if count1!=count2:
            anagram = False
            break
        i +=1
    if anagram:
        print("Anagram string")
    else:
        print("not anagram string")
            