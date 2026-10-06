s=input()
opening_brackets=0
missmached=0
for i in range(len(s)):
    if s[i]=="(":
        opening_brackets+=1
    if s[i]==")":
        if opening_brackets>0:
            opening_brackets-=1
        else:
            missmached+=1

print(missmached+opening_brackets)