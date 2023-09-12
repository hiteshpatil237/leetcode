class Solution(object):
    #One of the finest piece of code I've ever seen!
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n: #returning condition
                res.append("".join(stack))
                return

            if openN < n: #condition 1
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN: #condition 2
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res        