class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        bill5, bill10 = 0, 0
        for bill in bills:
            if bill == 5:
                bill5 += 1
            elif bill == 10:
                bill10 += 1
                if not bill5:
                    return False
                bill5 -= 1
            else:
                if bill10 and bill5:
                    bill10 -= 1
                    bill5 -= 1
                elif bill5 > 2:
                    bill5 -= 3
                else:
                    return False
        
        return True