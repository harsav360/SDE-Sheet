Problem Link -> https://leetcode.com/problems/two-sum/

def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = []
        for i in range(len(nums)):
            temp.append([nums[i],i])
        temp.sort(key = lambda x : x[0])
        first = 0
        second = len(temp)-1
        while first < second:
            if temp[first][0] + temp[second][0] == target:
                return [temp[first][1],temp[second][1]]
            elif temp[first][0] + temp[second][0] > target:
                second -= 1
            else:
                first += 1
