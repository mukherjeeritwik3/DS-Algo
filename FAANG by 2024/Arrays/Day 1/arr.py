



def containsCommonItem(arr1,arr2):

    
    # Brute Force

    # for i in arr1:
    #     for j in arr2:
    #         if i==j:
    #             print(True)

    # loop thru first arr1 and create an dictionary on it // o(n)
    dic = dict()
    for item in arr1:
        if(dic.get(item)!=True):
            dic[item] = True   
    #Loop thru 2nd loop and check the wheather present in dictionary or not // o(n)

    for item in arr2:
        if  dic.get(item)==True:
            return True
    return False

arr1 = ['a','b','c','d','a','b']
arr2 = ['x','y','z','d']
print(containsCommonItem(arr1,arr2))


