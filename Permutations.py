Problem Link - > https://leetcode.com/problems/permutations/description/

def permute(self, nums: List[int]) -> List[List[int]]:
        # def solve(ds,nums,ans,freq):
        #     if len(ds) == len(nums):
        #         ans.append(ds[:])
        #         return
        #     for i in range(len(nums)):
        #         if freq[i] == False:
        #             freq[i] = True
        #             ds.append(nums[i])
        #             solve(ds,nums,ans,freq)
        #             ds.pop()
        #             freq[i] = False
        # ans = []
        # ds = []
        # freq = [False for _ in range(len(nums))]
        # solve(ds,nums,ans,freq)
        # return ans

        def solve(index,nums,ans):
            if index == len(nums):
                ans.append(nums[:])
                return
            for i in range(index,len(nums)):
                swap(i,index,nums)
                solve(index+1,nums,ans)
                swap(i,index,nums)
        def swap(i,j,nums):
            nums[i],nums[j] = nums[j],nums[i]
        ans = []
        solve(0,nums,ans)
        return ans
