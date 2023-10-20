class Solution:
    def reverseWords(self, s: str) -> str:
        ans = list(s.strip().split())
        ans.reverse()
        return " ".join(ans)