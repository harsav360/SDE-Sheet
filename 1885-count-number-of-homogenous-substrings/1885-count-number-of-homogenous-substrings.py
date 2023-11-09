class Solution:
    def countHomogenous(self, s: str) -> int:
        ans,right,count = 0,0,0
        mod = pow(10,9)+7
        prev = ""
        while right < len(s):
            if prev == "":
                prev = s[right]
                count += 1
            elif prev == s[right]:
                count += 1
            else:
                ans += ((count*(count+1))//2)
                count = 1
                prev = s[right]
            right += 1
        ans += ((count*(count+1))//2)
        ans = ans%mod
        return ans