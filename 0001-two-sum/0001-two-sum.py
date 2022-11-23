class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = 0
        i = 0
        length = len(nums)
        
        for i, num in enumerate(nums):
            for idx in range(i+1, length):
                
                res = nums[i]+nums[idx]
                if res == target:
                    return [i, idx]
            