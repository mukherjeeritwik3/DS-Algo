

def mergeSortedArray(a,b):
    
    if (a==[]):
        return b
    if (b==[]):
        return a   
    c=[]


    idx1=0
    idx2=0 
    while(True): # o(n+m)?
        if((idx1 == len(a)) and (idx2==len(b))): 
            break;
        elif ( idx1 == len(a)):
            c.append(b[idx2])
            idx2+=1
        elif (idx2==len(b)):
            c.append(a[idx1])
            idx1+=1
        else:            
            if(a[idx1]>=b[idx2]):
                c.append(b[idx2])
                idx2+=1
            else:
                c.append(a[idx1])
                idx1+=1    
    return c            
arr1=[1,2,3,5,8,11]
arr2=[3,4,7,10,14]
print(mergeSortedArray(arr1,arr2))