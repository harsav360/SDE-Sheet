def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Brute Force approach is to traverse the whole Matrix. T:C -> O(N^2) and S:C -> O(1)

        # Better Approach is to use Binary Search, T:C -> O(NlogN) and S:C -> O(1)

        # def bs(arr):
        #     low,high = 0,len(arr)-1
        #     while low <= high:
        #         mid = (low+high)//2
        #         if arr[mid] == target:
        #             return True
        #         elif arr[mid] > target:
        #             high = mid-1
        #         else:
        #             low = mid+1
        #     return False
        # for i in range(len(matrix)):
        #     if bs(matrix[i]):
        #         return True
        # return False

        # Optimal Approach -> 1

        # n,m = len(matrix) , len(matrix[0])
        # i,j = 0,m-1
        # while i < n and j >= 0:
        #     if (matrix[i][j] == target):
        #         return True
        #     if (matrix[i][j] > target):
        #         j -= 1
        #     else:
        #         i += 1
        # return False

        # Optimal Approach -> 2

        n,m = len(matrix) , len(matrix[0])
        low,high = 0,(n*m)-1
        
        while low <= high:
            mid = (low + (high-low)//2)
            if (matrix[mid//m][mid%m]) == target:
                return True
            elif (matrix[mid//m][mid%m]) < target:
                low = mid+1
            else:
                high = mid-1
        return False
