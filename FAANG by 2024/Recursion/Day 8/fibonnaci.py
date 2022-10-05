def fiboIterative(n):
    first = 0
    second = 1
    if(n<2):
        return n
    
    for i in range(1,n):
        second, first = first+second , second
    return second

def fiboRecursive(n):
    if n <2:
        return n
    return fiboRecursive(n-1)+fiboRecursive(n-2)



print(fiboRecursive(4))
print(fiboIterative(8))