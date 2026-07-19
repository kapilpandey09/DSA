class Solution(object):
    def transformStr(self, s, strs):
        """
        :type s: str
        :type strs: List[str]
        :rtype: List[bool]
        """
        arr = {}
    
        
        for i in s:
            arr[i] = arr.get(i,0)+1

        dp = arr[:]

        res= []
        
        for st in strs:
            need = 0
            for let in st:
                if let in dp:
                    dp[let] -= 1
                else:
                    need+=1
            if dp['1']<0 or dp['0']<0:
                res.append(False)
            else:
                if dp['1'] > count:
                    res.append(False)
                elif dp['0'] > count:
                    res.append(False)
                elif dp['0'] == count:
                    if dp['1'] == 0:
                        res.append(True)
                elif dp['0'] < count:
                    if dp['1'] ==  (count-dp['0']):
                        res.append(True)
                    else:
                        res.append(False)
                
                
                    
                    
                    
                    
                
                
            
                    
            

        
            
        
                
        