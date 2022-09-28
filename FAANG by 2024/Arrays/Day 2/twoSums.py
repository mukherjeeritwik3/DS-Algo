nums = [2,5,5,11]
target = 10

dicts = dict()
for i in range(len(nums)):
    temp =target-nums[i]
    if nums[i] not in dicts:
        dicts[temp] = i
    else:
        print (dicts[nums[i]])
print([0,0])    