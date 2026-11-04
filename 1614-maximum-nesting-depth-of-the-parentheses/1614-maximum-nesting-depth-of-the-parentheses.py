class Solution:
    def maxDepth(self, s: str) -> int:
        level = 0
        count = 0
        for char in s:
            if char == '(':
                level += 1
                count = max(count, level)
            elif char == ')':
                level -= 1
        return count