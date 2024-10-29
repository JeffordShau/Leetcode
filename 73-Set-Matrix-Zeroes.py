class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        \\\
        Do not return anything, modify matrix in-place instead.
        \\\
        topRow = False
        leftColumn = False

        # record if topRow has 0
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                topRow = True
                break

        # record if leftColumn has 0
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                leftColumn = True
                break

        # record 0s in topRow and leftColumn
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # columns
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(len(matrix)):
                    matrix[j][i] = 0

        # rows
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0

        if topRow:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        if leftColumn:
            for i in range(len(matrix)):
                matrix[i][0] = 0