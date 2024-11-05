/*
 * @lc app=leetcode id=3232 lang=typescript
 *
 * [3232] Find if Digit Game Can Be Won
 */

// @lc code=start
function sum(arr: number[]): number {
  return arr.reduce((acc, curr) => acc + curr, 0);
}

function canAliceWin(nums: number[]): boolean {
  const res = false;
  const allSingle = nums.filter((num) => String(num).length === 1);
  const rest = nums.filter((num) => String(num).length !== 1);
  if (sum(allSingle) > sum(rest)) {
    return true;
  }

  const allDouble = nums.filter((num) => String(num).length === 2);
  const restDouble = nums.filter((num) => String(num).length !== 2);
  if (sum(allDouble) > sum(restDouble)) {
    return true;
  }

  return res;
}
// @lc code=end
