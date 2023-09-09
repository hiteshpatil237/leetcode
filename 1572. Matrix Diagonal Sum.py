class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        x = 0
        y = len(mat)-1
        dsum = 0
        for _ in range(len(mat)):
            if x == y:
                dsum += mat[x][x]
                x += 1
                y -= 1
                continue         
            dsum += (mat[x][x])
            dsum += (mat[x][y])
            x += 1
            y -= 1
        return dsum
        