s=input()
deph=0
score=0
for i in range(len(s)):
    if s[i]=="(":
        deph+=1
    if s[i]==")" and s[i-1]!="(":
        deph-=1
    if s[i]==")" and s[i-1]=="(":
        deph-=1
        score+=2**deph
print(score)
    
        