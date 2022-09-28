def sendLast(nums,target):
    temp = len(nums)-1
    i =0
    while(True):
        if(i==temp):
            nums[i] = target
            return nums
        if nums[i+1]==target:
            i+=1
        nums[i] = nums[i+1]
        i+=1
    return nums
testarr = [0,1,0,3,12]
print(sendLast(testarr,0))
print(sendLast(testarr,0))