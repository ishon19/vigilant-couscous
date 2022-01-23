function threeSum(nums: number[]): number[][] {
  nums = nums.sort((a, b) => a - b);
  const ans: number[][] = [];

  for (let i = 0; i < nums.length; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let l = i + 1;
    let r = nums.length - 1;

    while (l < r) {
      let sum = nums[i] + nums[l] + nums[r];
      if (sum > 0) {
        r--;
      } else if (sum < 0) {
        l++;
      } else {
        ans.push([nums[i], nums[l], nums[r]]);
        l++;
        if (nums[l] === nums[l - 1] && l < r) l++;
      }
    }
  }
  return ans;
}

console.log(threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]));
