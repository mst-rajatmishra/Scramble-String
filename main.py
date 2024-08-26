class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        n = len(s1)
        
        # dp[i][j][k] means if s1[i:i+k] can be scrambled to s2[j:j+k]
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]
        
        # Base case: single letter substrings
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]
        
        # Fill the DP table
        for length in range(2, n + 1):  # length of the substring
            for i in range(n - length + 1):  # start index in s1
                for j in range(n - length + 1):  # start index in s2
                    for k in range(1, length):  # split index
                        if (dp[i][j][k] and dp[i + k][j + k][length - k]) or \
                           (dp[i][j + length - k][k] and dp[i + k][j][length - k]):
                            dp[i][j][length] = True
                            break
        
        return dp[0][0][n]

