class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0 
        prod = 1
        con = 0
        n = len(nums)

        for ryt in range(n):
            prod *= nums[ryt]

            while prod >= k:
                prod /= nums[left]
                left += 1
            con += ryt - left + 1
        return con