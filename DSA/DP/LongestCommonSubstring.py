class Solution:
    
    def __init__(self):
        
        self.ans = 0
        self.dp = []
        self.s1 = ""
        self.s2 = ""
        
        
    def LCSTR(self,i,j):
        
        if(i<0 or j<0): return 0
        
        if(self.dp[i][j] != -1): return self.dp[i][j]
        
        
        self.dp[i][j] = 0
        
        if(self.s1[i] == self.s2[j]):
            
            self.dp[i][j] = 1 + self.LCSTR(i-1,j-1)
            
        
        nt1 = self.LCSTR(i,j-1)
        
        nt2 = self.LCSTR(i-1,j)
    
        self.ans = max(self.ans,self.dp[i][j])
        
        return self.dp[i][j]
    
    def longestCommonSubstr(self, S1, S2, n, m):
        
        self.dp = [[-1 for _ in range(m)] for _ in range(n)]
        
        self.s1 = S1
        self.s2 = S2
        
        self.LCSTR(n-1,m-1)
        
        return self.ans
    