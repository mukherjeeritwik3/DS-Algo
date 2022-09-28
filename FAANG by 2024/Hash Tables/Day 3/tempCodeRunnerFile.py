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