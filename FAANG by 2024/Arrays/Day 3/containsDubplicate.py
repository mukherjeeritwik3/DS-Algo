#Leet Code question - Easy

def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    hashset = set()
    hashset.c
    for i in nums:
        hashset.add(i)
    if (hashset.__len__()==len(nums)):
        return False
    return True
    

nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))