class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = list(set(nums))
        l.sort()
        if len(l) != 0:
            l.append(0)
        arr = []
        count = 0
        for i in range(len(l)):
            if i + 1 != len(l) and l[i+1] - l[i] != 1:
                arr.append(count+1)
                count = -1
            if count + 1 == len(l):
                arr.append(len(l))
            count += 1
        if len(l) == 0:
            return 0
        return max(arr)
        