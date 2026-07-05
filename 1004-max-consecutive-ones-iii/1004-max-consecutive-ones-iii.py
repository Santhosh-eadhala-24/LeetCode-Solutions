class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        left = 0
        zeroCo = 0
        for r in range(n):
            if nums[r] == 0:
                zeroCo += 1
            
            if zeroCo > k:
                if nums[left] == 0:
                    zeroCo -= 1
                left += 1
        return n - left