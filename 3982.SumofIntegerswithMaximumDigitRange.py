class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        
        best_diff = -1
        ans = 0

        for num in nums:
            x = abs(num)

            if x == 0:
                mn = mx = 0
            else:
                mn = 9
                mx = 0

                while x:
                    digit = x % 10
                    if digit < mn:
                        mn = digit
                    if digit > mx:
                        mx = digit
                    x //= 10

            diff = mx - mn

            if diff > best_diff:
                best_diff = diff
                ans = num
            elif diff == best_diff:
                ans += num

        return ans