class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pair = {}
        for i in range(len(nums)):
            if nums[i] in pair:
                pair[nums[i]] += 1
            else:
                pair[nums[i]] = 1
        for i in pair:
            if pair[i] > len(nums) / 2:
                return i