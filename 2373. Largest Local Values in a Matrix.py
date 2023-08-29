class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        def local(row, col):
            largest = 0
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if grid[i][j] > largest:
                        largest = grid[i][j]

            return largest

        maxLocal = []
        for i in range(len(grid) - 2):
            arr = []
            for j in range(len(grid) - 2):
                arr.append(local(i, j))
            maxLocal.append(arr)

        return maxLocal
