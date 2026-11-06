class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        sign = 1
        res = 0

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        while i < len(s) and s[i] == ' ':
            i += 1

        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1

        while i < len(s) and '0' <= s[i] <= '9':
            digit = int(s[i])
            res = res * 10 + digit
            i += 1

        res = res * sign

        if res < INT_MIN:
            return INT_MIN
        elif res > INT_MAX:
            return INT_MAX

        return res