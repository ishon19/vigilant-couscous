// Leetcode 238. Product of Array Except Self

function productExceptSelf(nums: number[]): number[] {
  let result: number[] = [];
  let left: number = 1;
  let right: number = 1;
  for (let i = 0; i < nums.length; i++) {
    result[i] = left;
    left *= nums[i];
  }
  for (let i = nums.length - 1; i >= 0; i--) {
    result[i] *= right;
    right *= nums[i];
  }
  return result;
}

console.log(productExceptSelf([1, 2, 3, 4]));