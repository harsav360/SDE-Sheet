class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack = []
        # ans = 0
        # for i in range(len(heights)):
        #     curr = heights[i]
        #     count = 0
        #     while stack and stack[-1] > curr:
        #         count += 1
        #         ans = max(ans,count*stack.pop())
        #     stack.append(curr)
        # count = 0
        # while stack:
        #     count += 1
        #     ans = max(ans,count*stack.pop())
        # return ans

        n = len(heights)
        left = [0]*n
        right = [0]*n

        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) == 0:
                left[i] = 0
            else:
                left[i] = stack[-1] + 1
            stack.append(i)
        while stack:
            stack.pop()
        for j in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[j]:
                stack.pop()
            if len(stack) == 0:
                right[j] = n-1
            else:
                right[j] = stack[-1]-1
            stack.append(j)
        ans = 0
        for i in range(n):
            ans = max(ans,heights[i]*(right[i]-left[i]+1))
        return ans

        