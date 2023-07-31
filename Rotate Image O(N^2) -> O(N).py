Problem Link -> https://leetcode.com/problems/rotate-image/description/

def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Brute Force Solution using Extra Space of O(N^2)

        # row,col = len(matrix),len(matrix[0])
        # tempM = [[0 for i in range(col)] for j in range(row)]

        # for c in range(col):
        #     for r in range(row):
        #         tempM[c][r] = matrix[row-1-r][c]

        # for r in range(row):
        #     for c in range(col):
        #         matrix[r][c] = tempM[r][c]

        # Optimal Approach

        row = len(matrix)

        # Take the transpose
        for i in range(row-1):
            for j in range(i+1,row):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        # Reverse each row of matrix
        for i in range(row):
            matrix[i].reverse()
