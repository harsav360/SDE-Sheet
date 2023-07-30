Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Brute Force Approach

        # row = len(matrix)
        # col = len(matrix[0])
        # for i in range(row):
        #     for j in range(col):
        #         if matrix[i][j] == 0:
        #             for k in range(col):
        #                 if matrix[i][k] == 0:
        #                     continue
        #                 else:
        #                     matrix[i][k] = '#'
        #             for p in range(row):
        #                 if matrix[p][j] == 0:
        #                     continue
        #                 else:
        #                     matrix[p][j] = '#'

        # for i in range(row):
        #     for j in range(col):
        #         if matrix[i][j] == '#':
        #             matrix[i][j] = 0

        # Better Approach

        # r,c = len(matrix),len(matrix[0])
        # row,col = [0]*r,[0]*c
        # for i in range(r):
        #     for j in range(c):
        #         if matrix[i][j] == 0:
        #             row[i] = 1
        #             col[j] = 1

        # for i in range(r):
        #     for j in range(c):
        #         if row[i] or col[j]:
        #             matrix[i][j] = 0

        # Optimal Approach

        r,c = len(matrix),len(matrix[0])
        col0 = 1

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        col0 = 0
                    else:
                        matrix[0][j] = 0

        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(c):
                matrix[0][j] = 0
        if col0 == 0:
            for i in range(r):
                matrix[i][0] = 0
