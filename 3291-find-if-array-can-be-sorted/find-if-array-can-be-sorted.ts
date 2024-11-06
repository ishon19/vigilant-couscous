function canSortArray(nums: number[]): boolean {
  // create a temp array storing the count of set bits for each number
  const bitArr = nums
    .map((num) => [num, num.toString(2).split("1").length - 1])
    .sort((a, b) => {
      if (a[1] === b[1]) {
        return a[0] - b[0]; // Sort by value if set bits are the same
      }
      return 0; // Do not change order if set bits are different
    });

  const temp = bitArr.map((item) => item[0]);

  // Use a copy of nums for sorting to avoid modifying the original array
  const sortedNums = [...nums].sort((a, b) => a - b);

  return JSON.stringify(sortedNums) === JSON.stringify(temp);
}