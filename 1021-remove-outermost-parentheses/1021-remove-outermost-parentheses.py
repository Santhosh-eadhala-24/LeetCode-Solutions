class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""

        lev = 0

        for char in s:
            if char == '(':
                if lev > 0:
                    res += char
                lev += 1
            elif char == ')':
                lev -= 1
                if lev > 0:
                    res += char
        return res