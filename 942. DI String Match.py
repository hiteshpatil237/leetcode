class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        nums = [0]
        for i in range(1, len(s) + 1):
            nums.append(nums[i - 1] + 1)
        
        res = []
        for c in s:
            left, right = 0, len(nums) - 1
            if c == "I":
                perm = nums.pop(left)
                left += 1
            else:
                perm = nums.pop(right)
                right -= 1
            res.append(perm)

        res.append(nums[0])
        return res                