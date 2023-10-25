class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Brute Force Approach

        # def solve(rem,index):
        #     if index >= n:
        #         table[:] = rem
        #         return
        #     temp = []
        #     for i in rem:
        #         if i == 0:
        #             temp.append(0)
        #             temp.append(1)
        #         else:
        #             temp.append(1)
        #             temp.append(0)
        #     rem[:] = temp
        #     solve(rem,index+1)

        # table = []
        # solve([0],1)
        # return table[k-1]

        # Optimized Approach using Binary Tree and Binary Search
        cur = 0
        left,right = 1,2**(n-1)
        for _ in range(n-1):
            mid = (left+right)//2
            if k <= mid:
                right = mid
            else:
                left = mid+1
                cur = 0 if cur else 1
        return cur
        