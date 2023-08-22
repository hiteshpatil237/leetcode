class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            
            count += (1 if n == res else -1)
        
        return res