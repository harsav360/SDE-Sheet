Problem Link -> https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

def maxLen(self, n, arr):
        #Code here
        # ans = 0
        # for i in range(n):
        #     total = 0
        #     for j in range(i,n):
        #         total += arr[j]
        #         if total == 0:
        #             ans = max(ans,j-i+1)
        # return ans
        
        mp = {}
        sum_ = 0
        maxLen = 0
        for i in range(n):
            sum_ += arr[i]
            if sum_ == 0:
                maxLen = max(maxLen,i+1)
            rem = sum_
            if rem in mp:
                len_ = i-mp[rem]
                maxLen = max(maxLen,len_)
            if sum_ not in mp:
                mp[sum_] = i
        return maxLen
