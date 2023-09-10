class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        ans = 0

        for c in s:
            if c == "(":
                stack.append(c)
                ans = max(ans, len(stack))
            elif c == ")":
                stack.pop()
        
        return ans