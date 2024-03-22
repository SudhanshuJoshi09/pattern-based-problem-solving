impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let n = text1.len();
        let m = text2.len();

        let text1 = text1.as_bytes();
        let text2 = text2.as_bytes();

        let mut dp: Vec<Vec<i32>> = vec![vec![0; m + 1]; n + 1];
        for i in (0..n).rev() {
            for j in (0..m).rev() {
                // Note: Using text1.chars().nth(i) is costly because we need to prepare an interator every time text1.chars() is called.
                let result = if text1[i] == text2[j] {
                    dp[i + 1][j + 1] + 1
                } else {
                    dp[i][j + 1].max(dp[i + 1][j])
                };
                dp[i][j] = result;
            }
        }
        return dp[0][0];
    }
}

