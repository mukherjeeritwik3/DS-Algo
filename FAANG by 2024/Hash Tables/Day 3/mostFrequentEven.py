#Leet Code - Easy

def mostFrequentEven(nums):
     """
    :type nums: List[int]
    :rtype: int
     """
     dicts = dict()
     sets = []

     for i in range(len(nums)):
          if nums[i]%2==0:
               if nums[i] in dicts:
                    dicts[nums[i]] = dicts.get(nums[i])+1
               else:
                    dicts[nums[i]] = 1
                    sets.append(nums[i]) 
     if dicts == {}:
          return -1
     maxed = max(dicts.values())
     sets.sort()
     for i in sets:
          if dicts[i] == maxed:
               return i

nums = [4369,3347,7166,1792,9101,6887,4418,7038,5287,1630,9023,1368,8972,8092,1120,7050,8661,1297,3013,4504,9578,9399,6196,2383,8801,2120]

print(mostFrequentEven(nums))

    