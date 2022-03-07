function largestPerimeter(nums: number[]): number {
  nums = nums.sort((a, b) => b - a);
  let i = 0;
  while (i < nums.length - 2) {    
    if (nums[i] < nums[i + 1] + nums[i + 2]) {
      return nums[i] + nums[i + 1] + nums[i + 2];
    } else i++;
  }
  return 0;
}

console.log(largestPerimeter([1,2,1]));
