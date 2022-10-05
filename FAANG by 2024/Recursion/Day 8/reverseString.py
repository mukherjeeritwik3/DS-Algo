def reverseStr(s):
    if s=="":
        return ""
        
    return reverseStr(s[1:]) + s[0]    



s = "hello"    
print(reverseStr(s))