#coding: utf-8


class Solution:
    def removeDuplicates(self, nums):
        """
        def removeDuplicates(self, nums: List[int]) -> int:
        """
        if not nums:
            return len(nums)
        finger = 0
        for i in range(0, len(nums) - 1):
            if nums[finger] != nums[finger + 1]:
                finger = finger + 1
            else:
                nums.pop(finger + 1)
        return len(nums)
    