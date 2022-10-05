#LeetCode - Easy

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        dub =1
        curr = nums[0]
        for i in range(1,len(nums)):
            if nums[i] !=curr:
                curr = nums[i]
                
                nums[dub] = curr
                dub+=1
                k+=1
        return k

nums = [0,0,1,1,1,2,2,3,3,4]

Solution().removeDuplicates(nums)
print(nums)
                