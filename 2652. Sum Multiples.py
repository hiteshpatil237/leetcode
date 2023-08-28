class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum([x for x in range(n + 1) if x % 3 == 0 or x % 5 == 0 or x % 7 == 0])