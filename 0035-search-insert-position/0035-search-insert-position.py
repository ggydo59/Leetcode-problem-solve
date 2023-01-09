class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            if nums[len(nums)-1] < target: return len(nums)
            for index, num in enumerate(nums):
                if nums[index] > target: return index
        else:
            for index, num in enumerate(nums):
                if nums[index] == target: return index