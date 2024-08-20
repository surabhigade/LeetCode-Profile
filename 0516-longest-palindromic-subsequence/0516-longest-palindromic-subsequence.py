class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        x = s
        y = s [::-1]
        m = len(x)
        n = len(y)
        
        # Initialize the tables to store the LCS lengths and backtrack information
        C = [[0] * (n + 1) for _ in range(m + 1)]
        # print(f"C: {C}")
        # S = [[""] * (n + 1) for _ in range(m + 1)]
        # print(f"S: {S}")
        # Fill the tables using the LCS-Length algorithm
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if x[i - 1] == y[j - 1]:
                    # If the current characters are the same, the length of the LCS is the length
                    # of the LCS of the substrings up to the previous characters plus 1, and
                    # the backtrack is " - ".
                    C[i][j] = C[i - 1][j - 1] + 1
                    # print(f"C1: {C}")
                    # S[i][j] = " topleft "
                    # print(f"S1: {S}")
                elif C[i - 1][j] >= C[i][j - 1]:
                    # If the length of the LCS of the substring up to the previous character
                    # in x is greater than or equal to the length of the LCS of the substring
                    # up to the previous character in y, the length of the LCS is the length
                    # of the LCS of the substring up to the previous character in x, and the
                    # backtrack is " ↑ ".
                    C[i][j] = C[i - 1][j]
                    # print(f"C2: {C}")
                    # S[i][j] = " ↑ "
                    # print(f"S2: {S}")
                else:
                    # Otherwise, the length of the LCS is the length of the LCS of the substring
                    # up to the previous character in y, and the backtrack is " ← ".
                    C[i][j] = C[i][j - 1]
                    # print(f"C3: {C}")
                    # S[i][j] = " ← "
                    # print(f"S3: {S}")
    
        return C[m][n]