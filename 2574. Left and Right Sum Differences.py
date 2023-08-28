class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        preSum = 0
        ans = []

        for i in range(len(nums)):
            leftSum = preSum
            rightSum = sum(nums) - preSum - nums[i]
            ans.append(abs(leftSum - rightSum))
            preSum += nums[i]
        
        return ans