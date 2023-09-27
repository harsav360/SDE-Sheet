class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for i in nums:
            dct[i] = 1 + dct.get(i,0)
        temp = []
        for key in dct.keys():
            temp.append([dct[key],key])
        temp.sort(reverse = True)
        ans = []
        i = 0
        while k:
            ans.append(temp[i][1])
            k -= 1
            i += 1
        return ans
        