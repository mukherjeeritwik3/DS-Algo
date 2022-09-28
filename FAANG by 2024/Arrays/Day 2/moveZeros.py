#LeetCode problem - Easy

def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        idxNonZero =0
        toZero =0

        for idx in range(len(nums)):
            if(nums[idx]!=0):
                nums[idxNonZero]=nums[idx]
                idxNonZero+=1
            else:
                toZero+=1  
            
        ne= -1   
        for i in range(toZero):
            nums[ne] =0
            ne-=1       
nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)
