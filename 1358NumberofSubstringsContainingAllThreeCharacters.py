class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        count = {'a': 0, 'b': 0, 'c': 0}

        i = 0
        ans = 0
        n = len(s)

        for j in range(n):
            count[s[j]] += 1

            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                ans += n - j
                count[s[i]] -= 1
                i += 1

        return ans