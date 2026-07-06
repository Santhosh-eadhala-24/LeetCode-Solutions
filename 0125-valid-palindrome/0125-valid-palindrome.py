class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        ryt = len(s) - 1

        while left < ryt :
            if not s[left].isalnum():
                left += 1
            elif not s[ryt].isalnum():
                ryt -= 1
            else:
                if s[left].lower() != s[ryt].lower():
                    return False
                left += 1
                ryt -= 1
        return True 