s=input()
opening_brackets_stack=[]
for i in range(len(s)):
    if s[i]=="(" or s[i]=="{" or s[i]=="[":
        opening_brackets_stack.append(s[i])
    else:
        print(ord(s[i]))
        
        if opening_brackets_stack[-1]==chr(ord(s[i])-1):
            opening_brackets_stack.pop()
        elif opening_brackets_stack[-1]==chr(ord(s[i])-2):
            opening_brackets_stack.pop()
        
if len(opening_brackets_stack)==0:
    print("true")
else:
    print("false")