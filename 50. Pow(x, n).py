def powRecur(x, n):
        if n == 0:
            return 1
        
        if n < 0:
            return 1 / powRecur(x, -1 * n)

        if n % 2 == 1:
            return x * powRecur(x * x, (n - 1) / 2)
        else:
            return powRecur(x * x, n / 2)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return powRecur(x, n)