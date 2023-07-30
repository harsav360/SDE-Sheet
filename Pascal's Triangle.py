def generate(self, numRows: int) -> List[List[int]]:
        # First Approach -> T:C -> O(N^3)

        # def ncr(row,col):
        #     ans = 1
        #     for i in range(col):
        #         ans = ans*(row-i)
        #         ans //= (i+1)
        #     return ans

        # ansRow = []
        # for row in range(1,numRows+1):
        #     temp = []
        #     for col in range(1,row+1):
        #         temp.append(ncr(row-1,col-1))
        #     ansRow.append(temp)
        # return ansRow

        # Optimal Approach -> O(N^2)

        def genRow(row):
            ans = 1
            ansRow = [1]

            for col in range(1,row):
                ans *= (row-col)
                ans //= col
                ansRow.append(ans)
            return ansRow

        result = []
        for i in range(1,numRows+1):
            result.append(genRow(i))
        return result
