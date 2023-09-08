class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        n, res, j, k = len(nums), 0, 1, 2

        for i in range(n - 2):
            while k < n and nums[k] < nums[i] + diff * 2:
                k += 1
            while j < k and nums[j] < nums[i] + diff:
                j += 1
            res += j < k < n and nums[k] - nums[j] == nums[j] - nums[i] == diff
            
        return res
        