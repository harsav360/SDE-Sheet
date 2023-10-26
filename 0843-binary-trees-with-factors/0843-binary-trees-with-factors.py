class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # First Sort the array
        arr.sort()
        # Declare an map to know the number of factors of particular number
        mp = {}
        mp[arr[0]] = 1 # For Smallest number, only one binary tree is possible(itself)
        for i in range(1,len(arr)):
            count = 1
            for key in mp.keys():
                if (arr[i]%key == 0 and arr[i]//key in mp):
                    count += mp[key]*mp[arr[i]//key]
            mp[arr[i]] = count
        result = 0
        modulo = 10**9+7
        for key in mp.keys():
            result = (result + mp[key])%modulo
        return result


        