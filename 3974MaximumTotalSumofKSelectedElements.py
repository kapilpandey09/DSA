class Solution(object):
    def maxSum(self, nums, k, mul):
        """
        :type nums: List[int]
        :type k: int
        :type mul: int
        :rtype: int
        """
        nums.sort(reverse=True)
        n = len(nums)
        val = min(n,k)
        res = 0
        for i in range(val):
            if mul > 0:
                res += nums[i]*mul
                mul -= 1
            else:
                res += nums[i]

        return res
            
        
        