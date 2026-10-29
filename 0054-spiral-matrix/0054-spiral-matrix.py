class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        top, bott = 0, m - 1
        left, ryt = 0, n - 1
        res = []

        while left <= ryt and top <= bott:
            for i in range(left, ryt + 1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bott + 1):
                res.append(matrix[i][ryt])
            ryt -= 1

            if top <= bott:
                for i in range(ryt, left - 1, -1):
                    res.append(matrix[bott][i])
                bott -= 1

            if left <= ryt:
                for i in range(bott, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res