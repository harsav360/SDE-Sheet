Problem Link -> https://leetcode.com/problems/trapping-rain-water/

def trap(self, height: List[int]) -> int:
        prefix = []
        prefix.append(height[0])
        maxi = height[0]
        n = len(height)
        for i in range(1,n):
            if maxi < height[i]:
                maxi = height[i]
            prefix.append(maxi)

        suffix = []
        suffix.append(height[-1])
        maxi2 = height[-1]
        for i in range(n-2,-1,-1):
            if maxi2 < height[i]:
                maxi2 = height[i]
            suffix.append(maxi2)
        suffix.reverse()
        
        ans = 0
        for i in range(n):
            ans += min(prefix[i],suffix[i]) - height[i]
        return ans
