class Solution:
    def findLucky(self, arr: List[int]) -> int:

        freq = {}

        for num in arr:
            freq[num] = freq.get(num,0)+1
        
        max_val = -1

        for key, val in freq.items():
            if key == val and max_val < key:
                max_val = key
        
        return max_val
        