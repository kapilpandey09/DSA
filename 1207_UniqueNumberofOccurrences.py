class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        res = {}

        for num in arr:
            res[num] = res.get(num,0)+1
        
        check = set()
        for key, value in res.items():
            if value not in check:
                check.add(value)
            else:
                return False
        return True


        