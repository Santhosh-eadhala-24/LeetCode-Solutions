class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palin(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        left = 0
        ryt = len(s) - 1

        while left < ryt:
            if s[left] != s[ryt]:
                return is_palin(left + 1,ryt) or is_palin(left, ryt - 1)
            left += 1
            ryt -= 1
        return True