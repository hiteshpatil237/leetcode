class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s)> len(t):
            for i in s:
                if s.count(i)>t.count(i):
                    return(i)
                    break
        if len(t)>len(s):
            for i in t:
                if t.count(i)>s.count(i):
                    return(i)
                    break