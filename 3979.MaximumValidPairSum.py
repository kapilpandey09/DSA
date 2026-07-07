class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)

        b = nums[0]
        res = float("-inf")
        
        for i in range(k,n):
            b = max(b,nums[i-k])
            res = max(res, b+nums[i])
                                            
        return res