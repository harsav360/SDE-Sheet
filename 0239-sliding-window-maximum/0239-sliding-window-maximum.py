class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # BFA 
        # ans = []
        # for i in range(k-1,len(nums)):
        #     check = -100000
        #     for j in range(i,i-k,-1):
        #         check = max(check,nums[j])
        #     ans.append(check)
        # return ans

        ans = []
        dq = deque()

        for i in range(len(nums)):
            while len(dq) != 0 and dq[0] == i-k:
                dq.popleft()
            while len(dq) != 0 and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                ans.append(nums[dq[0]])
        return ans


        