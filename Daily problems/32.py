s=input()
count_open_brackets=1
brackets=0
ar=[]
a=s.index("(")

for i in range(a+1,len(s)):
    if count_open_brackets!=0:
        if s[i]=="(":
            count_open_brackets+=1
            print(count_open_brackets)
        if s[i]==")":
            count_open_brackets-=1
            brackets+=1
    else:
        ar.append(brackets)
        brackets=0
print(ar)     
print(max(ar)*2)