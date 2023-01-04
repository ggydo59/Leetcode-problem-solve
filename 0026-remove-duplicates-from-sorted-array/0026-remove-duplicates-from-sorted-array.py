class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l1 = len(nums)
        temp = list(set(nums))
        temp.sort()
        l2 = len(temp)
        
        for i, value in enumerate(temp):
            nums[i] = value
        
        return l2