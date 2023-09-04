class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def recur(s, i):
            if i >= len(s) // 2:
                return
            
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
            recur(s, i + 1)

        recur(s, 0)