class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        firstPtr, secondPtr = 0, 0
        sizeFirst, sizeSecond = len(firstList), len(secondList)

        while firstPtr < sizeFirst and secondPtr < sizeSecond:
            if secondList[secondPtr][0] <= firstList[firstPtr][1] and firstList[firstPtr][0] <= secondList[secondPtr][1]:
                temp = [max(firstList[firstPtr][0], secondList[secondPtr][0]), min(firstList[firstPtr][1], secondList[secondPtr][1])]
                res.append(temp)

            if firstList[firstPtr][1] > secondList[secondPtr][1]:
                secondPtr += 1
            else:
                firstPtr += 1

        return res