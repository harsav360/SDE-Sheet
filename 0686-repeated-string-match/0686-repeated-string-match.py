class Solution:
    BASE = 1000000

    def repeatedStringMatch(self, A, B):
        if A == B:
            return 1
        count = 1
        source = A
        while len(source) < len(B):
            count += 1
            source += A
        if source == B:
            return count
        if self.Rabin_Karp(source, B) != -1:
            return count
        if self.Rabin_Karp(source + A, B) != -1:
            return count + 1
        return -1

    def Rabin_Karp(self, source, target):
        if source == "" or target == "":
            return -1
        m = len(target)
        power = 1
        for i in range(m):
            power = (power * 31) % self.BASE
        targetCode = 0
        for i in range(m):
            targetCode = (targetCode * 31 + ord(target[i])) % self.BASE
        hashCode = 0
        for i in range(len(source)):
            hashCode = (hashCode * 31 + ord(source[i])) % self.BASE
            if i < m - 1:
                continue
            if i >= m:
                hashCode = (hashCode - ord(source[i - m]) * power) % self.BASE
            if hashCode < 0:
                hashCode += self.BASE
            if hashCode == targetCode:
                if source[i - m + 1:i - m + 1 + m] == target:
                    return i - m + 1
        return -1


        