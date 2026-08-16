text=input("Enter an text:: ")
i=0
for ch in text:
    if ch in "aeiouAEIOU":
        i+=1
print("The total vowels in this word ::",i)        