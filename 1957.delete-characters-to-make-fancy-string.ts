/*
 * @lc app=leetcode id=1957 lang=typescript
 *
 * [1957] Delete Characters to Make Fancy String
 */

// @lc code=start
function makeFancyString(s: string): string {
  const stack: string[] = [];

    for (const char of s) {
      if(stack.length < 2 || stack[stack.length - 1] !== char || stack[stack.length - 2] !== char) {
        stack.push(char);
      } else {
        continue;
      }
  }

  return stack.join("");
}
// @lc code=end
