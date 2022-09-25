

arr1 = [1,2,3,4,5,9] # sum =8
arr2 = [78,2,1,2,4,4] #sum =8


#need to find if in array's pair sum is equal to 8 or not and return true or false
# input = array
# output = Boolean 

def getPairSum_check(arr, sum):
    # Brute force / Naive Solution
    # for i in range(len(arr)):
    #     for j in range(i+1,len(arr)):
    #         temp =arr[i]+arr[j]
    #         if(temp==sum):
    #             return True
    # return False
    
    # Better Solution if sorted array
    #Select first and last element and pair sum them to copare with given sum if its lower than sum then incr first with +1
    # and if its higher than sum decr last by -1

    # first = 0
    # last = arr.__len__()-1

    # while(first<last):
    #     temp = arr[first] +arr[last]
    #     if(temp==sum):
    #         return True;
    #     elif (temp<sum):
    #         first+=1
    #     else:
    #         last-=1
    # return False

    # Solution Best when array is not sorted use hash map ideas
    # Loop thru each element and subtract it with sum and store in it a unordered set Then compare at each loop if the
    # complements in set is equal to elemnt then return tru or false acc to it

    sets = dict()
    for item in arr:
        if sets.get(item):
            return True
        temp = sum-item    
        sets[temp] = True    
    return False    
              
print(getPairSum_check(arr1,8))