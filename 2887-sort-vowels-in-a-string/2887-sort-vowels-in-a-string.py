class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(['A','E','I','O','U','a','e','i','o','u'])
        temp = []
        for i in s:
            if i in vowels:
                temp.append(i)
        if len(temp) > 1:
            temp.sort()
        print(temp)
        s = list(s)
        j = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = temp[j]
                j += 1
        return "".join(s)
        