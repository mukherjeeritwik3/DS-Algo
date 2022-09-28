

def reverseString(str):
    if (len(str)==1):
        return str
    arr = [char for char in str] # o(n)
    first = 0 
    last = len(arr)-1

    while(first<last): #o(n/2)
        temp = arr[first]
        arr[first] =arr[last]
        arr[last] = temp
        first+=1
        last-=1
    return "".join(arr)    
str =  "Hi My name Is Ritwik"    
print(reverseString(str)) 
   