class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def ncr(n,r):
            res = 1
            for i in range(r):
                res = res * (n-i)
                res //= (i+1)
            return res

        ans = []
        for c in range(1,rowIndex+2):
            ans.append(ncr(rowIndex,c-1))
        return ans
        