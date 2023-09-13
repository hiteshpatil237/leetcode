class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] <= nums[r]:
                res = min(res, nums[mid])
                r = mid - 1
            else:
                l = mid + 1
        
        return res