class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq = {}

        for i in range(1, n+1):

            total = 0
            num = i

            while num:
                total += num % 10
                num //=10
            
            freq[total] = freq.get(total,0)+1
        
        mx = max(freq.values())

        ans = 0

        for count in freq.values():
            if count == mx:
                ans += 1
        return ans

        