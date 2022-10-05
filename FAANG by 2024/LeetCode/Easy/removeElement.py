#leetCode - Easy
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ht = dict()
        k = 0
        lastPointer = len(nums)-1
        for i in range(len(nums)):
            if lastPointer<= len(nums)//2:
                print(nums)
                if len(nums)==1:
                    return 0
                return len(nums)-k
            if nums[i] == val:
                while (True):
                    if nums[lastPointer] == val:
                        k+=1
                        lastPointer-=1
                    else:
                        break

                nums[lastPointer] , nums[i]= nums[i], nums[lastPointer]
                lastPointer-=1
                k+=1
        
        return len(nums)-k 

nums = [3,3]

print(Solution().removeElement(nums,3))
