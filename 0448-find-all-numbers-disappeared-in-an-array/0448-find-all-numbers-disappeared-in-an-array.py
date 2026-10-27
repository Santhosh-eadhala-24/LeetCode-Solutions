class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        i = 0
        n = len(nums)

        while i < n:
            crt_idx = nums[i] - 1
            if nums[i] != nums[crt_idx]:
                nums[i], nums[crt_idx] = nums[crt_idx], nums[i]
            else:
                i += 1
        res = []
        for i in range(n):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res
                