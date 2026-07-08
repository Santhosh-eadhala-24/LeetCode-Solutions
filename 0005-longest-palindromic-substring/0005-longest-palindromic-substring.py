class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        resLen = 0
        res = ""

        for i in range(len(s)):
            l , r = i ,i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen :
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1


            left , ryt = i , i + 1
            while left >= 0 and ryt < len(s) and s[left] == s[ryt]:
                if ryt - left + 1 > resLen :
                    res = s[left : ryt + 1]
                    resLen = ryt - left + 1
                left -= 1
                ryt += 1

        return res