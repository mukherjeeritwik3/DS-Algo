#Leet Code Ques - Medium 


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    a = nums.copy()

    for i in range(len(nums)):
        rem = (i+k)%len(nums)
        nums[rem] = a[i]
nums = [1,2,3,4,5,6,7]
rotate(nums,3)
print(nums)              