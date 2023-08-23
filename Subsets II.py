Problem Link -> https://leetcode.com/problems/subsets-ii/description/


def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # n = len(nums)
        # def solve(index,subset):
        #     if index == n:
        #         subset.sort()
        #         ans.add(tuple(subset))
        #         return
        #     subset.append(nums[index])
        #     solve(index+1,subset)
        #     subset.pop()
        #     solve(index+1,subset)
        # ans = set()
        # solve(0,[])
        # return ans

        res = []
        nums.sort()
        def dfs(idx, path):
            res.append(path)
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, path+[nums[i]])
        dfs(0, [])
        return res
