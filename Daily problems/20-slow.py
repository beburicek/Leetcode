class Solution(object):
    def isValid(self, s):
            opening_brackets_stack=[]
            if len(s)%2!=0:
                return False
            for i in range(len(s)):
                if s[i]=="(" or s[i]=="{" or s[i]=="[":
                    opening_brackets_stack.append(s[i])
                else:
                    if len(opening_brackets_stack)!=0:                    
                        if opening_brackets_stack[-1]==chr(ord(s[i])-1):
                            opening_brackets_stack.pop()
                        elif opening_brackets_stack[-1]==chr(ord(s[i])-2):
                            opening_brackets_stack.pop()
                        else:
                            return False
                    else:
                        return False
                    
            if len(opening_brackets_stack)==0:
                return True
            else:
                return False