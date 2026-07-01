class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        nums.sort()

        m =  nums[-1]
        count = 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] != nums[i+1]:
                count += 1
                if count == 3:
                    return nums[i]
        return m 
            
     