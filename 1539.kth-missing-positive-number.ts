/*
 * @lc app=leetcode id=1539 lang=typescript
 *
 * [1539] Kth Missing Positive Number
 */

// @lc code=start
function findKthPositive(arr: number[], k: number): number {
    let idx = 0;
    let left = 0;
    let right = arr.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] - mid - 1 < k) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return left + k;
}
// @lc code=end
