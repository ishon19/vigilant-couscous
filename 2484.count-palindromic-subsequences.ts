/*
 * @lc app=leetcode id=2484 lang=typescript
 *
 * [2484] Count Palindromic Subsequences
 */

// @lc code=start
function countPalindromes(s: string): number {
  const res = 0;
  const dp = Array.from({ length: s.length }, () =>
    Array.from({ length: s.length }, () => 0)
  );
    
    for (let i = 0; i < s.length; i++) {
        dp[i][i] = 1;
    }

    for (let len = 2; len <= s.length; len++) {
        for (let i = 0; i < s.length - len + 1; i++) {
            const j = i + len - 1;
            if (s[i] === s[j]) {
                let left = i + 1;
                let right = j - 1;
                while (left <= right && s[left] !== s[i]) {
                    left++;
                }
                while (left <= right && s[right] !== s[i]) {
                    right--;
                }
                if (left > right) {
                    dp[i][j] = dp[i + 1][j - 1] * 2 + 2;
                } else if (left === right) {
                    dp[i][j] = dp[i + 1][j - 1] * 2 + 1;
                } else {
                    dp[i][j] = dp[i + 1][j - 1] * 2 - dp[left + 1][right - 1];
                }
            } else {
                dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1];
            }
            dp[i][j] = (dp[i][j] + 1000000007) % 1000000007;
        }
    }

  return res;
}
// @lc code=end
