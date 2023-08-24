Problem Link -> https://leetcode.com/problems/combination-sum-ii/

def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # Giving TLE
        # def solve(index,target):
        #     if index == len(candidates):
        #         if target == 0:
        #             ds.sort()
        #             ans.add(tuple(ds[:]))
        #             return
        #         return
        #     if index > len(candidates) or target < 0:
        #         return
        #     ds.append(candidates[index])
        #     solve(index+1,target-candidates[index])
        #     ds.pop()
        #     solve(index+1,target)
        # ans = set()
        # ds = []
        # candidates.sort()
        # solve(0,target)
        # return ans

        ans,ds = [],[]
        candidates.sort()


        def findCombination(index,target):
            if target == 0:
                ans.append(ds[:])
                return
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                ds.append(candidates[i])
                findCombination(i+1,target-candidates[i])
                ds.pop()
        findCombination(0,target)
        return ans
