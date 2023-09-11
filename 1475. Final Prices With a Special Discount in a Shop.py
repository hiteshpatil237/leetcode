class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0] * len(prices)

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                res[stack.pop()] = prices[i]

            stack.append(i)
        
        ans = []
        for i in range(len(prices)):
            ans.append(prices[i] - res[i])
        
        return ans