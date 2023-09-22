class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        count = 0
        text = ""
        for i in s:
            
            if i == " ":
                count += 1
            if count == k:
                break
            text += i
        return text   