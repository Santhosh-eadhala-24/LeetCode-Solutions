class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def bs(nums,target,is_searching):
            i = 0
            j = len(nums) - 1
            idx = -1
            while i <= j:
                mid = i + (j - i) // 2

                if nums[mid] < target:
                    i = mid + 1
                elif nums[mid] > target:
                    j = mid - 1
                else:
                    idx = mid
                    if is_searching:
                        j = mid - 1
                    else:
                        i = mid + 1
            return idx
        
        left = bs(nums,target,True)
        ryt = bs(nums,target,False)
                
        return [left , ryt]