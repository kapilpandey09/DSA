class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:

        
        arr = []
        
        for i in range(m):
            if i == 0:
                arr.append("."*n)
            else:
                arr.append("#"*(n-1) + ".")
        
        return arr
                
            