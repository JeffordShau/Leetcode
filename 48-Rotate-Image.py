class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        \\\
        Do not return anything, modify matrix in-place instead.
        \\\
        # len(matrix) // 2 layers
        for i in range(len(matrix) // 2):
            # iterate across the top row
            for j in range(i, len(matrix) - i - 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[len(matrix) - j - 1][i]
                matrix[len(matrix) - j - 1][i] = matrix[len(matrix) - i - 1][len(matrix) - j - 1]
                matrix[len(matrix) - i - 1][len(matrix) - j - 1] = matrix[j][len(matrix) - i - 1]
                matrix[j][len(matrix) - i - 1] = temp