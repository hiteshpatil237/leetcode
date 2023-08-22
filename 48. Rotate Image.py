class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        for i in range(len(matrix)):
            for j in range(len(matrix) / 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix) - j - 1]
                matrix[i][len(matrix) - j - 1] = temp