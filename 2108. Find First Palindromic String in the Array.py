class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            l, r = 0, len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    break
                else:
                    l += 1
                    r -= 1
            else:
                return word
        else:
            return ""