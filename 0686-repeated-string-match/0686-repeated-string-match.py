class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        # Language ki akad ka solution
        temp = ""
        count = 0
        while len(temp) < len(B):
            temp += A
            count += 1
            if B in temp:
                return count
        temp += A
        if B in temp:
            return count + 1
        return -1

        