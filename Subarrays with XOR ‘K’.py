Problem Link -> https://www.codingninjas.com/studio/problems/subarrays-with-xor-k_6826258?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

def subarraysWithSumK(a: [int], b: int) -> int:
    # Write your code here
    # ans = 0
    # n = len(a)
    # for i in range(n):
    #     res = 0
    #     for j in range(i,n):
    #         res ^= a[j]
    #         if res == b:
    #             ans += 1
    # return ans

    # Optimal Approach 
    # 1. Map, x = xr^k and counting of there occurences 
    from collections import defaultdict
    n = len(a)
    cnt = 0
    xr = 0
    mp = defaultdict(int)
    mp[xr] = 1
    for i in range(n):
        xr = xr^a[i]
        x = xr^b
        cnt += mp[x]
        mp[xr] += 1
    return cnt
