class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        a = []
        s = 0
        n = len(nums)
        for i in range(n):
            s = s + nums[i]
            a.insert(i,s)

        return a
    