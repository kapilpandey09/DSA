class Solution:
    def minLights(self, lights: list[int]) -> int:

        n = len(lights)

        diff = [0] * (n + 1)

        for i, v in enumerate(lights):
            if v:
                l = max(0, i - v)
                r = min(n - 1, i + v)

                diff[l] += 1
                if r + 1 < len(diff):
                    diff[r + 1] -= 1

        ans = 0
        cur = 0
        s = 0

        for i in range(n):
            cur += diff[i]

            if cur == 0:
                s += 1
            else:
                ans += (s+2)//3
                s = 0
        ans += (s+2)//3

        return ans
        