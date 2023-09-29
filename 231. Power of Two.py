class Solution(object):
    def isPowerOfTwo(self, n, i = 0):
        """
        :type n: int
        :rtype: bool
        """
        if 2 ** i == n:
            return True

        if 2 ** i > n:
            return False
        
        return self.isPowerOfTwo(n, i + 1)