class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum=0        
        x=0
        while x<len(s):
            if x<len(s)-1 and a[s[x]]<a[s[x+1]]:
                sum += (a[s[x+1]] - a[s[x]])
                x += 2
            else:
                sum += a[s[x]]
                x += 1
        return sum