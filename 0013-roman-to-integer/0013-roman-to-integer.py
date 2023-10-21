class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {
            'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
            'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900
        }
        ans,i = 0,0
        n = len(s)
        while i < n:
            if i+1 < n and dct[s[i]] < dct[s[i+1]]:
                ans += dct[s[i:i+2]]
                i += 2
            else:
                ans += dct[s[i:i+1]]
                i += 1
        return ans
        