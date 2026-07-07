class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n = len(nums)
        val = nums[n//2]

        for i in range(n):

            if val == nums[i] and i != n//2:
                return False
        return True
                
                
        
        