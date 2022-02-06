function rearrangeArray(nums: number[]): number[] {
  const pos: number[] = [];
  const neg: number[] = [];
  const ans: number[] = [];

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 0) pos.push(nums[i]);
    else neg.push(nums[i]);
  }

  // merge
  let i = 0,
    j = 0;
  while (i < pos.length && j < neg.length) {
    ans.push(pos[i++]);
    ans.push(neg[j++]);
  }

  return ans;
}

console.log(rearrangeArray([6, -1, -2, -3, 4, 5]));
