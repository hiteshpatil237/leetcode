class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch in word:
            k = word.index(ch)
            chars = list(word)
            left, right = 0, k
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
            res = ''.join(chars)
            return res
        else:
            return word