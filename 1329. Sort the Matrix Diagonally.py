class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        d = {}

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i - j in d:
                    d[i - j].append(mat[i][j])
                else:
                    d[i - j] = [mat[i][j]]
        
        for k in d.keys():
            d[k].sort()
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = d[i - j].pop(0)

        return mat