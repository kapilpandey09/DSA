class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0)+1

        
        res = 1

        if 1 in freq :
            if freq[1] % 2 == 0:
                res = freq[1] - 1
            else:
                res = freq[1]

        
        for f in freq:
            num = f
            if num == 1:
                continue

           
            count = 1


            while( freq.get(num,0) >= 2):
                
                num *= num
                count += 2
            
            if freq.get(num,0) == 1:
                res = max(res, count)
            else:
                res = max(res, count - 2)
        
        return res
            

        