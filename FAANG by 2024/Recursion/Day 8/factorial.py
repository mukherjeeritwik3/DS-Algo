def factorialIterative(num):
    ans = 1
    temp = num
    for i in range(1,num):
        ans*=temp
        temp-=1
    return ans    

def factorialRecursive(num):
    if num ==1 or num==0:
        return 1
    return num*factorialRecursive(num-1)
print(factorialRecursive(0))
