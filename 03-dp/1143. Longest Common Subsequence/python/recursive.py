class Solution:
    def lcs_impl(self, text1, text2, idx1, idx2, dp):
        if len(text1) == idx1 or len(text2) == idx2:
            return 0

        if dp[idx1][idx2] != -1:
            return dp[idx1][idx2]
        

        result = self.lcs_impl(text1, text2, idx1, idx2 + 1, dp)
        result = max(result, self.lcs_impl(text1, text2, idx1 + 1, idx2, dp))

        if text1[idx1] == text2[idx2]:
            result = max(result, self.lcs_impl(text1, text2, idx1 + 1, idx2 + 1, dp) + 1)

        dp[idx1][idx2] = result
        return result

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for i in range(len(text2))] for j in range(len(text1))]
        return self.lcs_impl(text1, text2, 0, 0, dp)
