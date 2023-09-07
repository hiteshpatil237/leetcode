class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        
        if n == 1:
            return True
        else:
            if n % 3 == 0:
                k = n / 3
                return self.isPowerOfThree(k)

            return False