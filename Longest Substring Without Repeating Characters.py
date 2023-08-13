Problem Link -> https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        mp = {}
        left,right = 0,0
        n = len(s)
        while right < n:
            if s[right] in mp:
                ans = max(ans,right-left)
                while s[right] in mp:
                    mp.pop(s[left])
                    left += 1
            mp[s[right]] = 1
            right += 1
        ans = max(ans,len(mp))
        return ans
