class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = 0
        n = len(num) -1
        ind = -1
        for i in range(n, -1 , -1):
            if int(num[i]) % 2 == 1:
                ind = i
                break

        i = 0
        while i <= ind and num[i] =='0':
            i += 1

        word = num[i : ind + 1]
        return word