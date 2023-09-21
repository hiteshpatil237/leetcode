class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num > 0:
            num = num // 2 if num % 2 == 0 else num - 1
            steps += 1
        return steps