class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = {}
        for i in s:
            mp[i] = 1 + mp.get(i,0)
        for j in t:
            if j in mp:
                mp[j] -= 1
                if mp[j] == 0:
                    mp.pop(j)
            else:
                return False
        return len(mp) == 0
        
        